from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse
from django.contrib.auth import login

from users.mixins import UserActionMixin
from users.forms import SigninForm


class SigninView(UserActionMixin, FormView):
    template_name = "users/signin.html"
    form_class = SigninForm
    success_msg = "Signin Success"

    def form_valid(self, form):
        login(self.request, form.get_authenticated_user())
        return super(SigninView, self).form_valid(form)

    def get_success_url(self):
        return self.request.POST.get("next") or reverse("home")
