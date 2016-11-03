from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from posts.models import Post


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "posts/detail.html"
    context_object_name = "post"
