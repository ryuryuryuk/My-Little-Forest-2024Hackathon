from django.shortcuts import render, redirect
from django.http import JsonResponse
from start.models import User 
from .models import Custom_group, Tag

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
        # # 디버그 출력
        # print(f"tag1: {tag1}, tag2: {tag2}, tag3: {tag3}")
        # print(f"group_name: {group_name}, group_text: {group_text}")
        # print(f"group_img: {group_img}")

        try:  
            # Custom_group에 데이터 저장
            group = Custom_group.objects.create(
                constructor = request.session['nickname'],
                image = group_img,
                group_name = group_name,
                description = group_text
            )
            # tag에 데이터 저장  
            tags = [tag1, tag2, tag3]
            for tag in tags:
                Tag.objects.create(group_name = group.group_name, tag = tag) #group_id = group에서 group_id는 group 객체를 받고 내부적으로 group 객체의 pk를 추출하여 tag.group_id에 저장함
            # 성공 시 처리
            return JsonResponse({"success": True, 'message': '그룹 만들기 성공'}, status=200)
        except Exception as e:
            return JsonResponse({"success": False, 'message': '그룹 만들기 실패'}, status=404)

    return render(request, 'networking/makeGroup.html') 

def tagSearch(request):
    return render(request, 'networking/tagSearch.html') 
