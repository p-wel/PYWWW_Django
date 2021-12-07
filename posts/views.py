from django.shortcuts import render
from posts.models import Post


def posts_list(request):
    posts = Post.objects.all()
    context = {'posts_list': posts}
    return render(request, "posts/list.html", context)


def post_details(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, "posts/details.html", {"post": post})