from django.urls import path
from . import views 

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('investing', views.investing, name='investing'),
    path('frugality', views.frugality, name='frugality'),
    path('creditcards', views.creditcards, name='creditcards'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('subscribe', views.subscribe, name='subscribe'),
    path('subscribe-thank-you', views.subscribe_thank_you, name='subscribe-thank-you'),
]

