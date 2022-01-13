from django.urls import path
from .views import book_details, books_list, add_book, handle_book_borrows

app_name = 'books'
urlpatterns = [
    path('borrows', handle_book_borrows, name="borrows_list"),
    path('<int:book_id>/borrows', handle_book_borrows, name="borrows"),
    path('<int:book_id>/', book_details, name="details"),
    path('add', add_book, name="add"),
    path('', books_list, name="list"),
]
