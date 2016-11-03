from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from posts.models import Post
from posts.mixins import PostActionMixin


class PostUpdateView(LoginRequiredMixin, PostActionMixin, UpdateView):
    template_name = "posts/update.html"
    success_msg = "Update Success"
    context_object_name = "post"
