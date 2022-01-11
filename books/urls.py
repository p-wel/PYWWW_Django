from django.urls import path
from .views import book_details, books_list

app_name = 'books'
urlpatterns = [
    path('<int:book_id>/', book_details, name="details"),
    path('', books_list, name="list"),
]
