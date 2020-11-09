from django.urls import path, include

from common_app import views

urlpatterns = [
    path('', views.articles_list, name='articles')

]
