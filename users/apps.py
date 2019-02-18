from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'


#important tu import
    def ready(self):
        from users.signals import *
