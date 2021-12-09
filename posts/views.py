from django.shortcuts import render
from posts.models import Post


def posts_list(request):
    posts = Post.objects.filter(published=True)
    context = {'posts_list': posts}
    return render(request, "posts/list.html", context)


def post_details(request, post_id):
    post = Post.objects.get(pk=post_id)
    context = {}
    if post.published:
        context["post"] = post
    return render(request, "posts/details.html", context)
