from django.shortcuts import render, redirect
from django.http import JsonResponse
from start.models import User 
from sharing.models import Post_content, Comment, Scrap
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404



#게시판 페이지 띄우기 
def sharingContents(request):
    posts = Post_content.objects.all().order_by('-id')  # 게시글을 최신순으로 가져오기
    total_slots = 9  # 항상 9개의 슬롯을 유지
    empty_slots = total_slots - len(posts) if len(posts) < total_slots else 0  # 빈 슬롯 계산

    context = {
        'posts': posts[:9],  # 최대 9개의 게시글만 전달
        'empty_slots': range(empty_slots),  # 빈 슬롯 수를 range로 전달
    }
    return render(request, 'sharing/sharingContents.html', context)


def postpage(request, pk):
    post = get_object_or_404(Post_content, pk=pk)
    return render(request, 'sharing/postpage.html', {'post': post})


#글쓰기 페이지 렌더링
def get_writeContents(request):
    return render(request, 'sharing/writeContents.html') 

#글쓰기 db에 업로드 로직
def writeContents_logic(request):
    if request.method == 'POST':
        title = request.POST.get('post-title')  # 제목
        content = request.POST.get('post-content')  # 본문
        image = request.FILES.get('image-upload')  # 이미지

        # 현재 로그인된 사용자
        user = request.user

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
            # print(f"데이터 저장 오류: {str(e)}")  # 디버깅용 출력
            return JsonResponse({"success": False, "message": f"게시글 등록 실패: {str(e)}"}, status=500)
    else:
        return JsonResponse({"success": False, "message": "잘못된 요청입니다."}, status=400)


#내 컨텐츠 페이지 렌더링
def myContents(request):
    return render(request, 'sharing/myContents.html') 

def postpage(request, pk):
    # 특정 ID(pk)를 가진 게시글 가져오기
    post = get_object_or_404(Post_content, pk=pk)
    return render(request, 'sharing/postpage.html', {'post': post})