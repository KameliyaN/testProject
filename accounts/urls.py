from django.urls import path, include

from accounts import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'),
    path('profile/<int:pk>', views.UserDetails.as_view(), name='user-profile')

]
