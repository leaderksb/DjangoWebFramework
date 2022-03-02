# 사용자가 접속하는 경로에 따라 접속 요청을 어떻게 누가 처리해 줄 것인가 라우팅 해주는 파일

from django.contrib import admin
from django.urls import path, include
from DjangoApp import views

urlpatterns = [
    path('', views.index),
    path('create/', views.create),
    path('read/<id>/', views.read),
    path('update/<id>/', views.update),
    path('delete/', views.delete)
]
