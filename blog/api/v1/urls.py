from django.urls import path

from api.v1.views.blog_post import (CreatePostView, DestroyPostView, PostListView,
                                    RetrievePostView, UpdatePostView)
from api.v1.views.post_like import ClearPostLikesView, DislakePostView, LikePostView

app_name = 'v1'

urlpatterns = [
    path(r'post/', PostListView.as_view(), name='post_list'),
    path(r'post/create/', CreatePostView.as_view(), name='post_create'),
    path(r'post/<int:pk>/', RetrievePostView.as_view(), name='post_retrieve'),
    path(r'post/<int:pk>/delete/', DestroyPostView.as_view(), name='post_delete'),
    path(r'post/<int:pk>/update/', UpdatePostView.as_view(), name='post_update'),
    # path(r'post/<int:pk>/like/', LikePostView.as_view(), name='post_like'),
    # path(r'post/<int:pk>/dislake/', DislakePostView.as_view(), name='post_dislake'),
    path(r'post/<int:pk>/clear-like/', ClearPostLikesView.as_view(), name='post_like_clear'),
]