
from django.conf.urls import url
from shelf.views import *


app_name = "shelf"

urlpatterns = [

    url(r'^authors/$', AuthorListView.as_view(), name='my_author_list'),
    url(r'^authors/(?P<author_id>\d+)/$', AuthorDetailView.as_view(), name='author_detail'),

    url(r'^books/$', BookListView.as_view(), name="books"),

]
