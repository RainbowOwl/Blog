from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.blog.models import Like, Post


class BasePostLikeView(APIView):
    model = Post

    def get_object(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except Post.DoesNotExist:
            return None

    def get(self, request, pk):
        obj = self.get_object(pk)
        if obj is not None:
            if obj.likes is not None:
                self.perform_operate(obj)
            else:
                obj.likes = Like.objects.create(count=self.default_value)
            obj.save()
            return Response(status.HTTP_200_OK)
        return Response(status.HTTP_404_NOT_FOUND)

    def perform_operate(self):
        raise NotImplementedError()


class LikePostView(BasePostLikeView):
    default_value = 1

    def perform_operate(self, obj):
        obj.likes.increase_count()


class DislakePostView(BasePostLikeView):
    default_value = -1

    def perform_operate(self, obj):
        obj.likes.decrease_count()


class ClearPostLikesView(BasePostLikeView):
    default_value = 0

    def perform_operate(self, obj):
        obj.likes.clear_count()