from django.shortcuts import render

def hello_world(request):
    return render(request, "main/hello_world.html")

def about(request):
    return render(request, 'main/about.html')
