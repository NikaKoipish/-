from django.urls import reverse_lazy

from article.models import Article
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView


class ArticleCreateView(CreateView):
    model = Article
    fields = ('title', 'content', 'preview')
    success_url = reverse_lazy('article:articles')


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title', 'content', 'preview')
    success_url = reverse_lazy('article:articles')


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('article:articles')


class ArticleListView(ListView):
    model = Article
    template_name = 'article/articles_list.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article/article_detail.html'
