from django.conf.urls import url

from .views import *


urlpatterns = [
    url(r'^signup/$', SignupView.as_view(), name="signup"),
    url(r'^signin/$', SigninView.as_view(), name="signin"),
    url(r'^signout/$', SignoutView.as_view(), name="signout"),
]
