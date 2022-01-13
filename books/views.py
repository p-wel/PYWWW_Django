from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone

from books.admin import BookBorrowForm
from books.forms import BookForm
from books.models import Book, Borrow


def books_list(request):
    books = Book.objects.all()
    context = {'books_list': books}
    return render(request, "books/list.html", context)


def book_details(request, book_id):
    book = Book.objects.get(pk=book_id)
    form = BookBorrowForm()
    form.helper.form_action = reverse("books:borrows", args=[book.id])
    return render(
        request=request,
        template_name="books/details.html",
        context={"book": book, "form": form}
    )


def add_book(request):
    form = BookForm()
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse("books:add"))
    return render(
        request=request,
        template_name="books/add.html",
        context={"form": form}
    )


def handle_book_borrows(request, book_id=None):
    user = request.user
    if request.method == "POST":
        if user.is_authenticated:
            if request.POST.get("borrow"):
                book = Book.objects.get(pk=book_id)
                Borrow.objects.create(
                    user=user,
                    book=book
                )
                book.available = False
                book.save()
                return HttpResponseRedirect(reverse("books:details", args=[book_id]))
            else:
                keys = [key for key in request.POST.keys() if key.startswith("book_")]
                key = int(keys[0].split("_")[1])
                book = Book.objects.get(pk=key)
                borrow = Borrow.objects.filter(user=user, book=book).last()
                if not borrow.return_date:
                    borrow.return_date = timezone.now()
                    borrow.save()
                    book.available = True
                    book.save()
                return HttpResponseRedirect(reverse("books:borrows_list"))
    if request.method == "GET":
        borrows = Borrow.objects.filter(user=user)
        return render(request, "books/borrows_list.html", {"borrows": borrows})
