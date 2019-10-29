from django import forms
from .models import Post
from tinymce import TinyMCE
from django.db import models


class PostForm(forms.ModelForm):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }

    class Meta:
        model = Post
        fields = '__all__'