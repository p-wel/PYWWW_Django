from django.urls import path
from .views import *

app_name = 'books'
urlpatterns = [
    path('<int:book_id>/', book_details, name="details"),
    path('', books_list, name="list"),
]

