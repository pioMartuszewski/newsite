from django.shortcuts import render
from django.views.generic import View
import json
from django.http import HttpResponse
from django.core import serializers

from .forms import *
from .models import Message
# Create your views here.

class HomePageView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse(render(request, "users\\home.html"))


class UserFormView(View):
    def get(self, request):
        form = UserForm()
        return render(request, "users\\login_form.html", {"form": form})


    def post(self, request):
        form = MessageForm(data=request.POST)
        # form.save()
        qs = User.objects.last()
        return HttpResponse(render(request, "library\\index.html", {"name": qs.name, "email": qs.email}))


class MessageFormView(View):
    def get(self, request, *args, **kwargs):
        form = MessageForm()
        return render(request, "users\\message.html", {"form": form})


    def post(self, request, *args, **kwargs):
        form = MessageForm(data=request.POST)
        form.save()
        qs = Message.objects.last()
        qs_all = Message.objects.all()
        #qs_all to JSON
        #qs_all = serializers.serialize('json', qs_all)
        #qs_all to XML
        qs_all = serializers.serialize('xml', qs_all)
        to_json = {
            'name': qs.name,
            'email': qs.email,
            'message': qs.message,
        }
        dump = json.dumps(to_json)
        #return HttpResponse(qs_all, content_type='application/json')
        return HttpResponse(dump, content_type='application/json')







