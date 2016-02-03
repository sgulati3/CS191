from django.shortcuts import get_object_or_404, render

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
