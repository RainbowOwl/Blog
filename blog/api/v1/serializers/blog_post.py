from rest_framework import serializers

from apps.blog.models import Post, Tag, Like


class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('count',)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('value',)


class PostSerializer(serializers.ModelSerializer):
    likes = PostLikeSerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'content', 'created', 'is_draft', 'likes', 'tags')