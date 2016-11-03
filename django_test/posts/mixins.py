from django.contrib import messages

from .models import Post


class PostActionMixin(object):
    model = Post
    fields = ["title", "content", "image"]

    @property
    def success_msg(self):
        return NotImplemented

    def form_valid(self, form):
        messages.success(
            self.request,
            self.success_msg,
        )
        return super(PostActionMixin, self).form_valid(form)

    def delete(self, request, *args, **kwargs):
        messages.success(
            self.request,
            self.success_msg,
        )
        return super(PostActionMixin, self).delete(request, *args, **kwargs)
