from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from pywww import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
    path('posts/', include('posts.urls')),
    path('', include('main.urls')),
    path('', include('register.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
