from django.shortcuts import render, get_object_or_404
from .models import Article

# Create your views here.


def article_list(request):
    articles = Article.objects.all()
    return render(request, "home.html", {"articles": articles})


def article_detail(request, pk):
    articles = get_object_or_404(Article, pk=pk)
    return render(request, "article_detail.html", {"article": articles})
