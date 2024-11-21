from django.shortcuts import render, redirect
from django.http import JsonResponse

def searchLocal(request):
    return render(request, 'searchLocal/searchLocal.html')
