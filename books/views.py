from django.shortcuts import render

from books.models import Book


def books_list(request):
    books = Book.objects.all()
    slownik = {'Polska': 'Warszawa', 'Hiszpania': 'Barcelona'}

    age = 24
    first_name = 'Pawel'
    children = ['Aniela', 'Rozalia', 'Julian']
    programming_languages = {
        'python': 'advanced',
        'php': 'advanced',
        'js': 'intermediate'
    }
    bookies = set(['Czysty kod', 'PostgreSQL Biblia'])
    context = {'books_list': books, 'liczba': 100, 'slownik': slownik,
               'age': age,
               'first_name': first_name,
               'children': children,
               'programming_languages': programming_languages,
               'bookies': bookies
               }

    return render(request, "books/list.html", context)
