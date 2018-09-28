from django.urls import path

from apps.blog.views import ListPostView, CreatePostView

app_name = 'blog'

urlpatterns = [
    path('', ListPostView.as_view(), name='index'),
    path('create', CreatePostView.as_view(), name='create'),
]