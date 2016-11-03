from django.conf.urls import url

from posts.api import *


urlpatterns = [
    url(r'^posts/$', PostListAPIView.as_view(), name="posts"),
    url(r'^posts/(?P<pk>\d+)/$', PostDetailAPIView.as_view(), name="post_detail"),
]
