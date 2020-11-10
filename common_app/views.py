import requests
from django.shortcuts import render

# Create your views here.
from common_app.models import Article


def homepage(request):
    # params = {
    #     'token': 'sgfnw2wtulfkxlbid2dg',
    #     'currency': 'EUR/USD USD/JPY GBP/USD AUD/USD USD/CAD'
    # }
    # api_result = requests.get('https://currencydatafeed.com/api/data.php', params)
    #
    # api_response = api_result.json()
    # currencies = api_response['currency']

    context = {
        'articles': Article.objects.all(),
        # 'currencies': currencies

    }


    return render(request, 'common_app/index.html', context)
