from django import forms

from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'location', 'text', 'post_type', 'url', 'photo',)
