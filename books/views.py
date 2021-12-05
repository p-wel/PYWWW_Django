from django.http import HttpResponse


def library(request):
    return HttpResponse("Tu będzie moja biblioteka")
