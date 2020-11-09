from django.shortcuts import render

# Create your views here.
from common_app.models import Article


def articles_list(request):
    context = {
        'articles': Article.objects.all()
    }
    return render(request, 'common_app/index.html', context)
