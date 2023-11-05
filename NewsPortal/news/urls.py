from django.urls import path
from .views import (PostsList, PostDetail, PostsList_with_search,
                    NewsCreate, ArticlesCreate, NewsUpdate, NewsDelete,
                    ArticlesUpdate, ArticlesDelete, subscriptions,)
from django.views.decorators.cache import cache_page


urlpatterns = [
   path('news/', cache_page(60*1)(PostsList.as_view()), name='post_list'),
   path('news/<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('news/search/', PostsList_with_search.as_view(), name='post_list_search'),
   path('news/create/', NewsCreate.as_view(), name='news_create'),
   path('news/<int:pk>/update/', NewsUpdate.as_view(), name='news_update'),
   path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
   path('articles/create/', ArticlesCreate.as_view(), name='articles_create'),
   path('articles/<int:pk>/update/', ArticlesUpdate.as_view(), name='articles_update'),
   path('articles/<int:pk>/delete/', ArticlesDelete.as_view(), name='articles_delete'),
   path('subscriptions/', subscriptions, name='subscriptions'),
]