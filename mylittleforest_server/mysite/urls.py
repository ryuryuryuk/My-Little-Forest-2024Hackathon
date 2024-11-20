"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from django.contrib import admin #admin모듈 불러오기
from django.urls import path, include #path, include 모듈 불러오기

urlpatterns = [
    path("admin/", admin.site.urls),
    path("start/", include("start.urls")), #start애플리케이션 url
    path("login/", include("login.urls")),

    #path("main/", include("main.urls")), 
]

#main status
