from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('post-book', post_book_view, name='post-book'),
]
