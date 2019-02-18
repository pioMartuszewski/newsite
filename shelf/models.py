from django.db import models

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)
    books = models.ManyToManyField('Book')

    def __str__(self):
        return "{first_name} {last_name}".format\
            (first_name=self.first_name, last_name=self.last_name)


class Publisher(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    isbn = models.CharField(max_length=15)
    publisher = models.ForeignKey('Publisher', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "{title}".format\
            (title=self.title)


