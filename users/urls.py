from django.conf.urls import url
from users.views import *


app_name = "users"

urlpatterns = [

    url(r'^login/$', UserFormView.as_view(), name='login'),
    url(r'^message/$', MessageFormView.as_view(), name='message'),
    url(r'^$', HomePageView.as_view(), name='home')
]
