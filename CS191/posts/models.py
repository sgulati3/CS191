from __future__ import unicode_literals

from django.db import models


# Uncomment the following line if you are having issues with python2
# @python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField(max_length=140)
    date = models.DateTimeField('date submitted')
    text = models.TextField()

    ARTICLE = 'AP' # Text Post (url not required)
    VIDEO = 'VP' # Video Post (url required)
    PHOTO = 'PP' # Single photo (url requird)
    SLIDES = 'SP' # Multiple photos (url required)

    # URL requirement monitored at form level not model level
    POST_TYPE_CHOICES = (
        ('AP', 'Article Post'),
        ('VP', 'Video Post'),
        ('PP', 'Photo Post'),
        ('SP', 'Slideshow Post'),
    )
    post_type = models.CharField(max_length=2, choices=POST_TYPE_CHOICES,
                                blank=False, default='AP')
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title
