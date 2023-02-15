from django.urls import path
from main.views import categories
from main.views import PostListView

urlpatterns = [
    path("categories/", categories, name="categories-list"),
    path("posts/", PostListView.as_view(), name="posts-list")
]
