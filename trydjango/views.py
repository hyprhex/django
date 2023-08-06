"""
To render web pages 
"""
import random
# from django.http import HttpResponse
from django.shortcuts import render
from articles.models import Article

def home_view(request):

    name = 'Salah'
    random_id = random.randint(1, 4)

    article_obj = Article.objects.get(id=2)

    context = {
        'title': article_obj.title,
        'id': article_obj.id,
        'content': article_obj.content,
    }

    return render(request, 'articles/index.html', context)