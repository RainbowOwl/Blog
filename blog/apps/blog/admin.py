from django.contrib import admin
from apps.blog.models import Post, Tag, Like


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'content', 'created')
    list_filter = ('title', 'content')
    list_select_related = ('author',)
    ordering = ('created',)
    search_fields = ('title', 'content')

    class Meta:
        model = Post


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    class Meta:
        model = Tag

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    class Meta:
        model = Like

