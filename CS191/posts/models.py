from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from tags.models import Tag
import datetime


class Post(models.Model):
    title = models.CharField(max_length=140)
    date = models.DateTimeField(default=datetime.datetime.now)
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
    url = models.URLField(null=True, blank=True)
    photo = models.ImageField(null=True, blank=True, upload_to='posts')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:detail', kwargs={'post_id': self.id})

    def get_tags_by_post(self):
        return Tag.objects.filter(post=self)

