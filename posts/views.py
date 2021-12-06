from django.http import HttpResponse
from django.shortcuts import render
from posts.models import Post


def first_post(request):
    post = Post.objects.first()
    html = '<h2>' + post.title + '</h2>'
    html += f'''<div>
        <small>Utworzono {post.created}, zmodyfikowano {post.modified} </small>
    </div>
    <div>
        <p>{post.content}</p>
    </div>
    '''
    return HttpResponse(html)


def posts_list(request):
    posts = Post.objects.all()
    context = {'posts_list': posts}
    return render(request, "posts/list.html", context)