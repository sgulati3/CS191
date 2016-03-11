from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'event_date', 'location', 'text', 'post_type', 'event', 'url', 'photo',)

class SearchForm(forms.Form):
    EVENT_TYPE_CHOICES = (
        ('NA', 'All Events'),
        ('BR', 'Baltimore Uprising'),
        ('FP', 'Ferguson Protests'),
        ('SL', 'Stand With Leah'),
    )

    query = forms.CharField(max_length=16, required=False, widget = forms.TextInput(attrs={'class': 'form-control'}))
    event = forms.ChoiceField(choices=EVENT_TYPE_CHOICES, required=True, label='Trending Event')
