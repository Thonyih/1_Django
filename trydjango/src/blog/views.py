from django.shortcuts import render

from .models import Article

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView
)

# Create your views here.

class ArticleListView(ListView):

    template_name= 'articles/article_list.html'

    queryset = Article.objects.all()

