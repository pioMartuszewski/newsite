from django.db import models
from shelf.models import Book

class BookLendManager(models.Manager):
    def get_queryset(self):
        from django.db.models import F
        return super().get_queryset().filter(total_store__gt=F('total_borrow')).annotate(
            name=F("book_item__title")
        ).values()

class BookLend(models.Model):
    book_item = models.OneToOneField(Book, null=True, on_delete=models.SET_NULL)
    total_store = models.PositiveSmallIntegerField(default=0)
    total_borrow = models.PositiveSmallIntegerField(default=0)
    lends = BookLendManager()
    objects = models.Manager()

    def isAvaible(self):
        return self.total_store - self.total_borrow > 0


    def actual_count(self):
        return self.total_store - self.total_borrow


    def __str__(self):
         return self.book_item.title


#Create your models here.
