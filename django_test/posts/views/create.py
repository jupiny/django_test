from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from posts.models import Post
from posts.mixins import PostActionMixin


class PostCreateView(LoginRequiredMixin, PostActionMixin, CreateView):
    template_name = "posts/create.html"
    success_msg = "Save Success"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostCreateView, self).form_valid(form)
