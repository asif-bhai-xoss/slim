from django.forms import ModelForm
from django import forms
from .models import *


class PostBookForm(ModelForm):
    image = forms.ImageField(required=True, error_messages={'invalid': "Image files only"}, widget=forms.FileInput)

    class Meta:
        model = BookModel
        fields = '__all__'
        exclude = ['publisher']
