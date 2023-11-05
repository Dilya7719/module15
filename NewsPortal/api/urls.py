from django.urls import path
from .views import (get_new, get_news, create_new, edit_new, delete_new)
from django.views.decorators.cache import cache_page


urlpatterns = [
   path('new/<int:pk>/', get_new),
   path('news/', get_news),
   path('create_new/', create_new),
   path('edit_new/<int:pk>/', edit_new),
   path('delete_new/<int:pk>/', delete_new),
]