from datetime import date

import requests
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.

from django.views.generic import CreateView, DetailView

from accounts.models import Profile
from common_app.forms import ArticleForm
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


class CreateArticleView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = "common_app/write_article.html"

    def form_valid(self, form):
        article = form.save(commit=False)
        # profile = Profile.objects.get(user_id=self.request.user.id)
        article.user = self.request.user.profile
        article.save()
        return redirect('home')


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    context_object_name = 'article'
    template_name = "common_app/view_article.html"


