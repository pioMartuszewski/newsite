from django.contrib import admin
from .models import *

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    pass


class MessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message']


admin.site.register(Message, MessageAdmin),
admin.site.register(User, UserAdmin),
