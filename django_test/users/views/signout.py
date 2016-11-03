from django.views.generic import RedirectView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import logout

from users.mixins import UserActionMixin


class SignoutView(UserActionMixin, RedirectView):

    success_msg = "Signout Success"
    url = reverse_lazy("home")

    def get_redirect_url(self, *args, **kwargs):
        logout(self.request)
        return super(SignoutView, self).get_redirect_url(*args, **kwargs)
