from django.shortcuts import render

from books.models import Book


def books_list(request):
    books = Book.objects.all()
    context = {'books_list': books}
    return render(request, "books/list.html", context)
