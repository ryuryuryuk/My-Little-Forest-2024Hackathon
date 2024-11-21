from django.shortcuts import render, redirect
from django.http import JsonResponse
from start.models import User 

def networking(request):
    return render(request, 'networking/networking.html') 
def makeGroup(request):
    return render(request, 'networking/makeGroup.html') 
def tagSearch(request):
    return render(request, 'networking/tagSearch.html') 
