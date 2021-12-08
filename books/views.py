from django.shortcuts import render
from books.models import Book


def books_list(request):
    books = Book.objects.all()
    context = {'books_list': books}
    return render(request, "books/list.html", context)

def book_details(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, "books/details.html", {"book": book})

