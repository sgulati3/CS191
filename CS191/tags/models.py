from __future__ import unicode_literals

from django.db import models
import datetime


class Tag(models.Model):
    title = models.CharField(max_length=16)
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE)
    votes = models.IntegerField(blank=True, default=0)
    date = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.title
