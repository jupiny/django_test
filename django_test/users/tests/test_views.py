from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model

from users.forms import SignupForm
from users.forms import SigninForm


class UserViewTests(TestCase):

    def setUp(self):
        get_user_model().objects.create_user(
            email="email1@example.com",
            password="Password1!",
        )
        get_user_model().objects.create_user(
            email="email2@example.com",
            password="Password2!",
        )
        self.signup_url = reverse("users:signup")
        self.signin_url = reverse("users:signin")
        self.signout_url = reverse("users:signout")

    def test_signup_page_renders_signup_template(self):
        response = self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/signup.html')

    def test_signup_page_uses_signup_form(self):
        response = self.client.get(self.signup_url)
        self.assertIsInstance(response.context['form'], SignupForm)

    def test_signup_success(self):
        post = {
            "email": "email3@example.com",
            "password1": "Password3!",
            "password2": "Password3!",
        }
        response = self.client.post(self.signup_url, post)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("home"))
        self.assertEqual(get_user_model().objects.count(), 3)

    def test_signup_by_preexisting_email(self):
        post = {
            "email": "email2@example.com",
            "password1": "Password3!",
            "password2": "Password3!",
        }
        response = self.client.post(self.signup_url, post)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(get_user_model().objects.count(), 2)
        self.assertFormError(
            response,
            "form",
            "email",
            "User with this Email already exists.",
        )

    def test_signin_page_renders_signn_template(self):
        response = self.client.get(self.signin_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/signin.html')

    def test_signin_page_uses_signin_form(self):
        response = self.client.get(self.signin_url)
        self.assertIsInstance(response.context['form'], SigninForm)

    def test_signin_success(self):
        data = {
            "email": "email1@example.com",
            "password": "Password1!",
        }
        response = self.client.post(self.signin_url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("home"))
        self.assertTrue(self.client.session.items())

    def test_signin_by_nonexistent_email(self):
        data = {
            "email": "email3@example.com",
            "password": "Password3!",
        }
        response = self.client.post(self.signin_url, data)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(
            response,
            "form",
            "password",
            "The email does not exist.",
        )

    def test_signin_by_wrong_password(self):
        data = {
            "email": "email1@example.com",
            "password": "Password2!",
        }
        response = self.client.post(self.signin_url, data)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(
            response,
            "form",
            "password",
            "The password is wrong.",
        )

    def test_signout(self):
        self.client.login(
            email="email1@example.com",
            password="Password1!"
        )
        self.assertTrue(self.client.session.items())

        response = self.client.get(self.signout_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("home"))
        self.assertFalse(self.client.session.items())
