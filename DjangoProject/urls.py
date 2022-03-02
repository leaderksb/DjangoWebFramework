"""DjangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# 사용자가 접속하는 경로에 따라 접속 요청을 어떻게 누가 처리해 줄 것인가 라우팅 해주는 파일

from django.contrib import admin
from django.urls import path, include

# http://127.0.0.1/
# http://127.0.0.1/app

# http://127.0.0.1/create
# http://127.0.0.1/read/1/

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('DjangoApp.urls'))  # admin이 아닌 다른 경로로 접속을 하면 DjangoApp.urls로 위임
]
