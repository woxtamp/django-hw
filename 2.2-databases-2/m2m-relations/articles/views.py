from django.shortcuts import render

from articles.models import Article, Tag, Scope


def articles_list(request):
    ordering = '-published_at'
    articles = Article.objects.all().prefetch_related('scopes').order_by(ordering)

    template = 'articles/news.html'

    context = {'object_list': articles}

    return render(request, template, context)