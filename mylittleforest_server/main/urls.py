from django.urls import path
from . import views

app_name = "main"

urlpatterns = [    
    path('', views.main, name='main'), # 로그아웃된 메인화면
    path('mainLogin_a/', views.mainLogin_a, name='mainLogin_a'), # 결과a로 로그인된 메인화면
    path('mainLogin_b/', views.mainLogin_b, name='mainLogin_b'), # 결과b로 로그인된 메인화면
]
