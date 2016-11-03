from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model

from users.validators import validate_minimum_length, validate_letters


class SignupForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Password',
        error_messages={'required': 'Please enter your password.'},
        validators=[
            validate_minimum_length,
            validate_letters,
        ],
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label='Password confirmation',
        error_messages={
            'required': 'Please enter your password confirmation.'
        },
        widget=forms.PasswordInput
    )

    class Meta:
        model = get_user_model()
        fields = [
            'email',
        ]

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['email'].error_messages = {
            'required': 'Please enter your email.',
            'unique': 'User with this Email already exists.',
            'invalid': 'Enter a valid email address.',
        }

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match.")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(SignupForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
