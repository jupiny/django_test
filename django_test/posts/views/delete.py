from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy

from posts.mixins import PostActionMixin


class PostDeleteView(LoginRequiredMixin, PostActionMixin, DeleteView):
    success_msg = "Delete Success"
    success_url = reverse_lazy("posts:list")
