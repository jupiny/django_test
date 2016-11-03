from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from posts.models import Post


class PostListView(LoginRequiredMixin, ListView):
    template_name = "posts/list.html"
    model = Post
    context_object_name = "posts"
