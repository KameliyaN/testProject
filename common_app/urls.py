from django.urls import path, include

from common_app import views

urlpatterns = [
    path('', views.homepage, name='home')

]
