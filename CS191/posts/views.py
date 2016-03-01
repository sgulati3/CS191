from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import PostForm
from .models import Post


def index(request):
    latest_post_list = Post.objects.order_by('date')[:5]
    context = {
        'latest_post_list': latest_post_list,
    }

    return render(request, 'posts/index.html', context)

def detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    context = {
        'post': post,
    }

    return render(request, 'posts/detail.html', context)

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.date = timezone.now()
            post.save()
            return redirect(post)
    else:
        form = PostForm()

    context = {
        'form': form,
    }

    return render(request, 'posts/create.html', context)
