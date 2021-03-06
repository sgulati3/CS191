# from django.contrib.gis.geoip import GeoIP
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.template.defaulttags import register

from .forms import PostForm
from .forms import SearchForm
from .models import Post
from tags.models import Tag
from collections import defaultdict

from itertools import groupby

import json


# Default page that displays all posts
def index(request):
    all_posts = Post.objects.all().order_by('event_date')
    grouped_posts = defaultdict(list)

    for post in all_posts:
        grouped_posts[post.event_date.date()].append(post)

    sorted_dates = list(grouped_posts.keys())
    sorted_dates.sort()

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

    tag_freq = {}
    for time_bucket in grouped_posts.keys():
        tagFreqInBucket = {}
        tagFreqInBucket = defaultdict(lambda:0, tagFreqInBucket)

        for post in grouped_posts[time_bucket]:
            for tag in Tag.objects.filter(post=post):
                tagFreqInBucket[tag.title]+=1

        tag_freq[time_bucket] = tagFreqInBucket

    context = {
        'form': SearchForm,
        'latest_post_list': all_posts,
        'tag_map': {post.id : post.get_tags_by_post() for post in all_posts},
        'tag_titles': None,
        'grouped_posts': grouped_posts,
        'sorted_dates': sorted_dates,
        'tag_freq': tag_freq
    }

    return render(request, 'posts/index.html', context)

# Detail view for a given post
def detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    tags = post.get_tags_by_post()
    context = {
        'post': post,
        'tags': tags,
        'tag_titles': json.dumps([tag.title for tag in tags]),
    }
    return render(request, 'posts/detail.html', context)

def search(request):
    form = SearchForm(request.POST)
    
    if (form.is_valid()):
        query = str(form.cleaned_data['query']).strip()
        event = str(form.cleaned_data['event'])
        tags = Tag.objects.filter(title__icontains=query)
        post_set = set()

        if query == "":
            for post in Post.objects.all():
                if event == 'NA' or post.event == event:
                    post_set.add(post)
        else:
            for tag in tags:
                if event == 'NA' or tag.post.event == event:
                    post_set.add(tag.post)

        post_list = list(post_set)
        grouped_posts = defaultdict(list)
        for post in post_list:
            grouped_posts[post.event_date.date()].append(post)

        context = {
            'form': SearchForm,
            'grouped_posts': grouped_posts,
            'tag_map': {post.id : post.get_tags_by_post() for post in post_list},
            'tag_titles': None
        }

        return render(request, 'posts/index.html', context)

    else:
        return index(request)

# Creating a new post object
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
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
    all_posts = Post.objects.all().order_by('event_date')
    context = {
        'all_posts': all_posts
    }
    return render(request, 'posts/board.html', context)

@register.filter
def get_value(dictionary, key):
    return dictionary.get(key)

@register.filter
def date_to_integer(dt_time, unused_parameter):
    return 10000*dt_time.year + 1000*dt_time.month + dt_time.day
