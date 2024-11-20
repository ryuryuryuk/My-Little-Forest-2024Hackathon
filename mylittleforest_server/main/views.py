from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
from .models import User #import .model.User

def main(request):
    return render(request, 'main/main.html') #로그아웃된 메인페이지
