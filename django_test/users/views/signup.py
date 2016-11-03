from django.views.generic.edit import CreateView
from django.conf import settings
from django.core.urlresolvers import reverse_lazy

from users.forms import SignupForm
from users.mixins import UserActionMixin


class SignupView(UserActionMixin, CreateView):
    template_name = "users/signup.html"
    form_class = SignupForm
    success_url = reverse_lazy("home")
    success_msg = "Signup Success"
