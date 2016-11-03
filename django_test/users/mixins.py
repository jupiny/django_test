from django.contrib import messages


class UserActionMixin(object):

    @property
    def success_msg(self):
        return NotImplemented

    def form_valid(self, form):
        messages.success(
            self.request,
            self.success_msg,
        )
        return super(UserActionMixin, self).form_valid(form)

    def get_redirect_url(self, *args, **kwargs):
        messages.success(
            self.request,
            self.success_msg,
        )
        return super(UserActionMixin, self).get_redirect_url(*args, **kwargs)
