from django.contrib import admin
from .models import BookLend

class BookLendAdmin(admin.ModelAdmin):
    list_display = ['book_item', 'total_store', 'total_borrow']
    #pass

admin.site.register(BookLend, BookLendAdmin)

# Register your models here.
