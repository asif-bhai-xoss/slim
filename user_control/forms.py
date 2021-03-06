from django import forms
from django.contrib.auth.forms import authenticate
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data.get('email')
            password = self.cleaned_data.get('password')
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Email or Password is incorrect")


class StudentRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=255, help_text='Required. Add a valid email address')
    name = forms.CharField(max_length=60)
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(),
        help_text='Password must contain at least 8 character including numeric values',
    )
    is_student = forms.BooleanField(widget=forms.HiddenInput(), initial=True)

    class Meta:
        model = User
        fields = ("name", "email", "password1", "password2", "is_student")


class PublisherRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=255, help_text='Required. Add a valid email address')
    name = forms.CharField(max_length=60)
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(),
        help_text='Password must contain at least 8 character including numeric values',
    )
    is_publisher = forms.BooleanField(widget=forms.HiddenInput(), initial=True)

    class Meta:
        model = User
        fields = ("name", "email", "password1", "password2", "is_publisher")
