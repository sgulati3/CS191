from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import PostForm
from .models import Post


def index(request):
    all_posts = Post.objects.all().order_by('date')
    paginator = Paginator(all_posts, 3) # Show 10 posts per page
    page_num = request.GET.get('page')

    try:
        paginated_posts = paginator.page(page_num)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        paginated_posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        paginated_posts = paginator.page(paginator.num_pages)

    context = {
        'latest_post_list': paginated_posts,
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
