
from django.contrib import admin
from django.urls import path, include

from .views import (
    article_create_view,
    article_detail_view,
    article_delete_view,
    article_list_view,
    blog_home_view,
)

app_name = 'Blog_app'
urlpatterns = [
    path('', blog_home_view, name = 'home'),
    path('all/', article_list_view, name = 'list-articles'),
    path('create/', article_create_view, name = 'create-article'),
    path('detail/<int:my_id>/', article_detail_view, name = 'article-detail'),
    path('delete/<int:my_id>/', article_delete_view, name = 'article-delete'),
]