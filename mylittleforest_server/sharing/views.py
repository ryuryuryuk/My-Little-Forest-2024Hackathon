from django.shortcuts import render, redirect
from django.http import JsonResponse
from start.models import User 
from sharing.models import Post_content, Comment, Scrap

def sharingContents2(request):
    return render(request, 'sharing/sharingContents2.html') 

def writeContents(request):
    return render(request, 'sharing/writeContents.html') 


def writeContents_logic(request):
    if request.method == 'POST':
        title = request.POST.get('post-title')  # 제목
        content = request.POST.get('post-content')  # 본문
        image = request.FILES.get('image-upload')  # 이미지

        # 입력값 검증
        if not title or not content:
            return JsonResponse({"success": False, "message": "제목과 본문은 필수 항목입니다."}, status=400)

        try:
            user = User.objects.get(nickname=request.session['nickname'])
        except User.DoesNotExist:
            return JsonResponse({"success": False, "message": "유효하지 않은 사용자입니다."}, status=400)

        # 이미지 검증
        if image and not image.content_type.startswith('image/'):
            return JsonResponse({"success": False, "message": "업로드된 파일은 이미지여야 합니다."}, status=400)

        # 데이터 저장
        try:
            post = Post_content.objects.create(
                author=user,
                title=title,
                content=content,
                image=image
            )
            return JsonResponse({"success": True, "message": "게시글 등록 성공"}, status=200)
        except Exception as e:
            print(f"데이터 저장 오류: {str(e)}")  # 디버깅용 출력
            return JsonResponse({"success": False, "message": f"게시글 등록 실패: {str(e)}"}, status=500)
    else:
        return JsonResponse({"success": False, "message": "잘못된 요청입니다."}, status=400)