# from django.contrib.gis.geoip import GeoIP
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import PostForm
from .models import Post
from tags.models import Tag


# Default page that displays all posts
def index(request):
    all_posts = Post.objects.all().order_by('-event_date')
    paginator = Paginator(all_posts, 5) # Show 5 posts per page
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
        'latest_post_list': all_posts,
        'tag_map': {post.id : post.get_tags_by_post() for post in paginated_posts}
    }

    return render(request, 'posts/index.html', context)

# Detail view for a given post
def detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    context = {
        'post': post,
        'tags': post.get_tags_by_post(),
    }
    return render(request, 'posts/detail.html', context)

# Creating a new post object
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.date = timezone.now()

            # Setting location
            # g = GeoIP()
            # ip = request.META.get('REMOTE_ADDR')
            # if ip:
            #     post.location = str(g.city(ip) + ", " + str(g.country(ip))
            # else:
            #     city = 'Rome'

            post.save()

            # add tags
            for i in range(0, int(request.POST.get("numTags"))):
                tagTitle = request.POST.get("hidden-tag-" + str(i))

                if (tagTitle != ''):
                    # Initialize tags with 1 vote
                    newTag = Tag.objects.create(title=tagTitle, post=post, votes=1)
                    newTag.save()

            return redirect(post)
    else:
        form = PostForm()

    context = {
        'form': form,
    }

    return render(request, 'posts/create.html', context)

def board(request):
    
    return render(request, 'posts/board.html')
