from django.shortcuts import render, get_object_or_404
from blog.models import BlogPosts

# Create your views here.


def all_blogs(request):
    posts = BlogPosts.objects.order_by('-date')
    return render(request, 'blog/all_blogs.html', {'posts' : posts})


def detail(request, post_id):
    post = get_object_or_404(BlogPosts, pk=post_id) #pk = primary key
    return render(request, 'blog/detail.html', {'post' : post})
