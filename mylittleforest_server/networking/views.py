from django.shortcuts import render, redirect
from django.http import JsonResponse
from start.models import User 

def networking(request):
    return render(request, 'networking/networking.html') 

def makeGroup(request):
    if request.method == 'POST':
        #텍스트 데이터 받기
        tag1 = request.POST.get('tag1')
        tag2 = request.POST.get('tag2')
        tag3 = request.POST.get('tag3')
        group_name = request.POST.get('group-name')
        group_text = request.POST.get('group_text')
        # 파일 데이터 받기
        group_img = request.FILES.get('group-img')
        # 디버그 출력
        print(f"tag1: {tag1}, tag2: {tag2}, tag3: {tag3}")
        print(f"group_name: {group_name}, group_text: {group_text}")
        print(f"group_img: {group_img}")
    return render(request, 'networking/makeGroup.html') 

def tagSearch(request):
    return render(request, 'networking/tagSearch.html') 
