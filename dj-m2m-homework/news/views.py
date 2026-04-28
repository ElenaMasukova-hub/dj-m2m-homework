from django.shortcuts import render, get_object_or_404
from .models import Article, Scope

def index(request):
    articles = Article.objects.all()
    return render(request, 'news/index.html', {'articles': articles})

def detail(request, id):
    article = get_object_or_404(Article, id=id)
    scopes = Scope.objects.filter(article=article).select_related('tag').order_by(
        '-is_main', 'tag__name'
    )
    return render(request, 'news/detail.html', {
        'article': article,
        'scopes': scopes
    })