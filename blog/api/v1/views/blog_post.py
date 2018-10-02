from rest_framework.generics import (CreateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework import permissions
from api.v1.serializers.blog_post import PostSerializer
from apps.blog.models import Post
from api.permissions import RoleIsAdministrator, RoleIsAdministratorOrManager


class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.AllowAny, )


class CreatePostView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (RoleIsAdministratorOrManager, )


class RetrievePostView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.AllowAny, )


class DestroyPostView(DestroyAPIView):
    queryset = Post.objects.all()
    permission_classes = (RoleIsAdministrator, )


class UpdatePostView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (RoleIsAdministratorOrManager, )