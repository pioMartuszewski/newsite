from django.db import models
from django.contrib.auth.models import User as DjangoUser

# Create your models here.


class User(models.Model):
    profile = models.OneToOneField(DjangoUser, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    login = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return "User: {name} {login}" .format\
            (name=self.name, login=self.login)


class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    # def __str__(self):
    #     return "Message from {name}" .format(name=self.name)

