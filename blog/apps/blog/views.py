from django.views.generic import ListView, CreateView
from django.urls import reverse

from apps.blog.models import  Post


class ListPostView(ListView):
    model = Post
    template_name = 'post_list.html'


class CreatePostView(CreateView):
    model = Post
    fields = ('title', 'content', 'is_draft', 'tags')
    template_name = 'post_edit.html'

    def get_success_url(self):
        return reverse('blog:index')