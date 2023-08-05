"""
To render web pages 
"""
import random
from django.http import HttpResponse
from articles.models import Article

def home_view(request):

    name = 'Salah'
    random_id = random.randint(1, 4)

    article_obj = Article.objects.get(id=random_id)

    context = {
        'title': article_obj.title,
        'id': article_obj.id,
        'content': article_obj.content,
    }

    HTML_STRING = """
    <h1>{title} (id: {id})</h1>
    <p>{content}</p>
    """.format(**context)

    return HttpResponse(HTML_STRING)