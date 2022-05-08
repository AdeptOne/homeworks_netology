from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    articles = Article.objects.all()

    context = {
        'articles': articles
    }

    return render(request, 'articles/news.html', context)
