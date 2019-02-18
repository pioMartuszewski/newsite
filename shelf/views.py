from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import ListView, View
#import z submodelu aplikacji
from .models import Author
from .models import Publisher
from .models import Book


class AuthorListView(View):
    def get(self, request):
        authors = Author.objects.all()
        return HttpResponse(render(request, "shelf\\my_author_list.html", {"authors": authors}))


class AuthorDetailView(View):
    def get(self, request, author_id):
        author = Author.objects.get(pk=author_id)
        return HttpResponse(render(request, "shelf\\author_detail.html", {"author": author}))
        # return render(request, 'shelf\\author_detail', {"author": author})


class BookListView(View):
    def get(self, request):
        allBooks = Book.objects.all()
        return HttpResponse(render(request, "shelf\\book_list.html", {"allBooks": allBooks}))


class BookDetailView(View):
    def get(self, request, book_id):
        book = Book.objects.get(pk=book_id)
        return HttpResponse(render(request, "shelf\\book_detail"))

class PublisherListView(ListView):
    pass


