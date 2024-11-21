from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
from start.models import User #import .model.User

def main(request):
    return render(request, 'main/main.html') #로그아웃된 메인페이지
def mainLogin_a(request):
    return render(request, 'main/mainLogin_a.html') #로그아웃된 메인페이지
def mainLogin_b(request):
    return render(request, 'main/mainLogin_b.html') #로그아웃된 메인페이지
