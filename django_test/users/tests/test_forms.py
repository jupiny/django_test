from django.test import TestCase
from django.contrib.auth import get_user_model

from users.forms import SignupForm
from users.forms import SigninForm


class UserFormTests(TestCase):

    def setUp(self):
        get_user_model().objects.create_user(
            email="email1@example.com",
            password="Password1!",
        )
        get_user_model().objects.create_user(
            email="email2@example.com",
            password="Password2!",
        )

    def test_signup_form_validation_success(self):
        form_data = {
            "email": "email3@example.com",
            "password1": "Password3!",
            "password2": "Password3!",
        }
        form = SignupForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_signup_form_validation_for_preexisting_email(self):
        form_data = {
            "email": "email2@example.com",
            "password1": "Password3!",
            "password2": "Password3!",
        }
        form = SignupForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['email'],
            ['User with this Email already exists.'],
        )

    def test_signup_form_validation_for_weak_password(self):
        form_data = {
            "email": "email3@example.com",
            "password1": "password!",
            "password2": "password!",
        }
        form = SignupForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['password1'],
            ['Password must contain at least 1 digit.'],
        )

    def test_signin_form_validation_success(self):
        form_data = {
            "email": "email1@example.com",
            "password": "Password1!",
        }
        form = SigninForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_signin_form_validation_for_nonexistent_email(self):
        form_data = {
            "email": "email3@example.com",
            "password": "Password1!",
        }
        form = SigninForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['password'],
            ['The email does not exist.'],
        )

    def test_signin_form_validation_for_wrong_password(self):
        form_data = {
            "email": "email1@example.com",
            "password": "Password2!!",
        }
        form = SigninForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['password'],
            ['The password is wrong.'],
        )
