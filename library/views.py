from .models import BookLend
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
import json


class HelloLibrary(View):
    def get(self, request):
        all_books = BookLend.objects.all()
        av_books = []
        for b in all_books:
            if b.isAvaible():
                av_books.append(b)
        return HttpResponse(render(request, "library\\index.html", {"books": all_books,
                                                                    "av_books": av_books}))

    # def get_ajax_books(self, request):
    #     qs = BookLend.objects.filter(self.total_store > self.total_borrow)
    #     qs = serializers.serialize('json', qs)
    #     return HttpResponse(qs, content_type="application/json")


# def get_ajax_books(request):
#     qs = BookLend.objects.all()
#     av_book = []
#     for b in qs:
#         if b.isAvaible():
#             av_book.append(b)
#     av_book = serializers.serialize('json', av_book)
#     return HttpResponse(av_book, content_type="application/json")


def get_ajax_books(request):
    qs = BookLend.lends.all()
    return HttpResponse(json.dumps(list(qs)), content_type='application/json')








