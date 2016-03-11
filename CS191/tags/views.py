from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Tag
from posts.models import Post


def create(request, post_id, tag_title):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=post_id)
        newTag = Tag.objects.create(title=tag_title, post=post, votes=1)

    return HttpResponse(status=204)

# Increment votes
def vote(request, post_id, tag_title):
    if request.method == 'POST':
        tag = get_object_or_404(Tag, post_id=post_id, title=tag_title)
        Tag.objects.select_for_update().filter(post_id=post_id, title=tag_title).update(votes=(tag.votes+1))

    return HttpResponse(status=204)

# Decrement votes
def unvote(request, post_id, tag_title):
    if request.method == 'POST':
        tag = get_object_or_404(Tag, post_id=post_id, title=tag_title)
        Tag.objects.select_for_update().filter(post_id=post_id, title=tag_title).update(votes=(tag.votes-1))

    return HttpResponse(status=204)
