from django import forms
from .models import User, Message


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name', 'login', 'email')


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('name', 'email', 'message')

