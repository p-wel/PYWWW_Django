from django.shortcuts import render

def hello_world(request):
    context = {'hello_text': 'Hello World!'}
    return render(request, "main/about.html", context=context)
