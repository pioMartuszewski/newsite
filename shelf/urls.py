from django.urls import path
from django.conf.urls import url
from shelf.views import *

app_name = "shelf"

urlpatterns = [
    #path('authors/', admin.site.urls),

    url(r'^all-authors/$', AuthorListView.as_view(), name='my_author_list'),
    url(r'authors/(?P<author_id>\d+)/$', AuthorDetailView.as_view(), name='author_detail'),

    url(r'^books/$', BookListView.as_view(), name="books"),
    path('publish/', PublisherListView.as_view()),

]
