from django import forms
from django.contrib.auth.models import User
from .models import Post


class CreatePostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ["title", "body"]


class EditPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ["title", "body"]
