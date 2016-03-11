from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from tags.models import Tag
import datetime


class Post(models.Model):
    title = models.CharField(max_length=140)
    event_date = models.DateTimeField(default=datetime.datetime.now)
    sub_date = models.DateTimeField(default=datetime.datetime.now)
    location = models.CharField(max_length=140)
    text = models.TextField()

    VIDEO = 'VP' # Video Post
    PHOTO = 'PP' # Single photo

    POST_TYPE_CHOICES = (
        ('VP', 'Video Post'),
        ('PP', 'Photo Post'),
    )
    post_type = models.CharField(max_length=2, choices=POST_TYPE_CHOICES,
                    blank=False, default='AP')


    EVENT_TYPE_CHOICES = (
        ('BR', 'Baltimore Uprising'),
        ('FP', 'Ferguson Protests'),
        ('SL', 'Stand With Leah'),
        ('NA', 'Not Currently Trending'),
    )
    event = models.CharField(max_length=2, choices=EVENT_TYPE_CHOICES,
                    blank=False, default='BR')

    url = models.URLField(null=True, blank=True)
    photo = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:detail', kwargs={'post_id': self.id})

    def get_tags_by_post(self):
        return Tag.objects.filter(post=self)

