from __future__ import unicode_literals

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=140)
    date = models.DateTimeField('date submitted')
    text = models.TextField()

    # If a URL is required, the frontend will ensure it gets created with one
    POST_TYPE_CHOICES = (
        ('AP', 'Article Post'), # Text Post (should not have url)
        ('VP', 'Video Post'), # Video Post (url required)
        ('PP', 'Photo Post'), # Single photo (url requird)
        ('SP', 'Slideshow Post'), # Multiple photos (url required)
    )
    post_type = models.URLField(max_length=2, choices=POST_TYPE_CHOICES,
                                blank=False, default='AP')
    url = models.URLField(default = None)
