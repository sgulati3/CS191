from django import forms

from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'event_date', 'location', 'text', 'post_type', 'event', 'url', 'photo',)

class SearchForm(forms.Form):
    query = forms.CharField(max_length=16)
