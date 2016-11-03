from django import forms
from django.contrib.auth import get_user_model, authenticate


class SigninForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        error_messages={'required': 'Please enter your Email.'},
    )
    password = forms.CharField(
        label='Password',
        error_messages={'required': 'Please enter your password.'},
        widget=forms.PasswordInput,
    )

    def clean_password(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        # Check that the email exists
        try:
            user = get_user_model().objects.get(email=email)
        except get_user_model().DoesNotExist:
            raise forms.ValidationError("The email does not exist.")
        # Check that the password is correct
        if not user.check_password(password):
            raise forms.ValidationError("The password is wrong.")
        return password

    def get_authenticated_user(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        user = authenticate(email=email, password=password)
        return user
