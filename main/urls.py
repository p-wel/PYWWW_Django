from django.urls import path
from main.views import *

app_name = 'main'
urlpatterns = [
    path('about', about, name='about'),
    path('', hello_world, name="hello_world"),
]
