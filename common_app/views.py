import requests
from django.shortcuts import render

# Create your views here.
from common_app.models import Article


def articles_list(request):
    params = {
        'token': 'sgfnw2wtulfkxlbid2dg',
        'currency': 'EUR/USD USD/JPY GBP/USD USD/CHF AUD/USD NZD/USD USD/CAD'
    }
    api_result = requests.get('https://currencydatafeed.com/api/data.php', params)

    api_response = api_result.json()
    currencies=api_response['currency']
    print(currencies)

    context = {
        'articles': Article.objects.all(),
        'currencies': currencies

    }

    # print(api_response)

    # params = {
    #     'apikey': 'ZX2ZPRW3YWJ9I49Z',}
    # base_url = r"https://www.alphavantage.co/query?function = CURRENCY_EXCHANGE_RATE"
    # main_url = base_url
    # req_ob = requests.get(base_url,params)
    # result = req_ob.json()
    # print(result)

    # params = {
    #     'access_key': '6debc7e077ca0ad17f00166e0093e432',
    #
    # }
    #
    # api_result = requests.get('http://api.marketstack.com/v1/currencies', params)
    #
    # api_response = api_result.json()
    # print(api_response)
    return render(request, 'common_app/index.html', context)
