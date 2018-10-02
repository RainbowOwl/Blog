from django.contrib import admin
from apps.blog.models import Post, Tag, Like
from blog.admin import portfolio_admin_site, PorfolioModelAdmin


class PostAdmin(PorfolioModelAdmin):

    list_display = ('edit_link', 'title', 'content', 'created')
    list_filter = ('title', 'content')
    list_select_related = ('author',)
    ordering = ('created',)
    search_fields = ('title', 'content')

    class Meta:
        model = Post


class TagAdmin(PorfolioModelAdmin):
    class Meta:
        model = Tag

class LikeAdmin(PorfolioModelAdmin):
    class Meta:
        model = Like

portfolio_admin_site.register(Post, PostAdmin)
portfolio_admin_site.register(Tag, TagAdmin)
portfolio_admin_site.register(Like, LikeAdmin)