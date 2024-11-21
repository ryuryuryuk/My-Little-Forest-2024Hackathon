from django.urls import path
from . import views

app_name = "networking"

urlpatterns = [
    path('', views.networking, name='networking'), 
    path('makeGroup/', views.makeGroup, name='makeGroup'), 
    path('tagSearch/', views.tagSearch, name='tagSearch'), 
]
