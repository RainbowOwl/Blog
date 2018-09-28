from django.db.models import Q
from django.urls import reverse
from django.views.generic import (CreateView, DeleteView, DetailView, ListView, TemplateView,
UpdateView)

from apps.blog.models import Post, Tag, Like


class ListPostView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query)
            ).distinct()
            self.paginate_by = None
        return queryset

class CreatePostView(CreateView):
    model = Post
    fields = ('title', 'content', 'is_draft', 'tags')
    template_name = 'post_edit.html'

    def get_success_url(self):
        return reverse('blog:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = reverse('blog:post-create')
        return context


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ('title', 'content', 'is_draft', 'tags')

    def get_success_url(self):
        return reverse('blog:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = reverse('blog:post-edit', kwargs={'pk': self.get_object().id})
        return context


class DeletePostView(DeleteView):
    model = Post
    template_name = 'post_delete.html'

    def get_success_url(self):
        return reverse('blog:index')


class DetailPostView(DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_absolute_url(self):
        return reverse('blog:post-detail', kwargs={'pk': self.id})


class ListTagView(ListView):
    model = Tag
    # template_name = 'tag_list.html'


class CreateTagView(CreateView):
    model = Tag
    # template_name = 'tag_edit.html'

    def get_success_url(self):
        return reverse('blog:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = reverse('blog:tag-create')
        return context


class UpdateTagView(UpdateView):
    model = Tag
    # template_name = 'tag_edit.html'

    def get_success_url(self):
        return reverse('blog:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = reverse('blog:tag-edit', kwargs={'pk': self.get_object().id})
        return context


class DeleteTagView(DeleteView):
    model = Tag
    # template_name = 'tag_delete.html'

    def get_success_url(self):
        return reverse('blog:index')


class DetailTagView(DetailView):
    model = Tag
    # template_name = 'tag_detail.html'

    def get_absolute_url(self):
        return reverse('blog:tag-detail', kwargs={'pk': self.id})


class SinglePageView(TemplateView):
    template_name = 'single_page_blog.html'