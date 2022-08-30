from django.urls import path
from django.shortcuts import render
from . import views

urlpatterns = [
    path('', views.news, name='news'),
    ]

def news(request):
    return render(request, 'news.html')
