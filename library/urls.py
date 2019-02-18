from django.conf.urls import url
from library.views import *


app_name = "library"

urlpatterns = [
    url(r'^$', HelloLibrary.as_view(), name='hello'),
    url(r'^ajax$', get_ajax_books, name='ajax_books'),
    # url(r'^ajax_xml$', get_ajax_avbooks, name='ajax_books_xml')

]