from django.urls import path
from . import views

app_name = "start"

urlpatterns = [
    # stating 페이지
    path('', views.starting, name='starting'), #start(app이름):starting(url이름)

    # 신규 회원 가입 과정
    path('startingName/', views.startingName, name='startingName'),
    path('startingName2/', views.startingName2, name='startingName2'),
    path('startingPrefer/', views.startingPrefer, name='startingPrefer'),
    path('startingInterest/', views.startingInterest, name='startingInterest'),
    path('startingJob/', views.startingJob, name='startingJob'),
    path('startingEnv/', views.startingEnv, name='startingEnv'),
    path('startingBudget/', views.startingBudget, name='startingBudget'),
    path('startingFam/', views.startingFam, name='startingFam'),
    
    # 결과 페이지 。。。

    
]
