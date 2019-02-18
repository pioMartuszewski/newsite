from django.contrib import admin
from .models import Author, Publisher, Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'isbn', 'publisher']
    ordering = ['title']


class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name']



admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Publisher, PublisherAdmin)



# Register your models here.
