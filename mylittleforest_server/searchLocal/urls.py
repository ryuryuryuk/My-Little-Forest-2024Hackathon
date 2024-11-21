from django.urls import path
from . import views

app_name = "searchLocal"

urlpatterns = [
    path('', views.searchLocal, name='searchLocal'),
]