from django.urls import path, include

from common_app import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('create_article/', views.CreateArticleView.as_view(), name='create article'),
    path('view_article/<int:pk>/', views.ArticleDetailView.as_view(), name='view article'),
    path('edit_article/<int:pk>/', views.ArticleUpdateView.as_view(), name='edit article'),

]
