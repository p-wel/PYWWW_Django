from django.urls import path
from .views import *

urlpatterns = [
    path('<int:post_id>/', post_details),
    path('', posts_list),
]
