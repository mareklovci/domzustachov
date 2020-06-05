from django.shortcuts import render

from .models import Article, Author


def index(request):
    articles = Article.objects.all()
    authors = Author.objects.all()

    data = {
        'articles': articles,
        'authors': authors,
    }

    return render(request, 'index.html', data)


def contact(request):
    data = {}
    return render(request, 'index.html', data)
