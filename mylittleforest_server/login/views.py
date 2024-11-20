from django.shortcuts import render, redirect
from django.http import JsonResponse
from start.models import User #import .model.User

# 로그인
def login(request): 
    if request.method == 'POST':
        #서버로 전송된 닉네임 이름을 db에서 조회
        nickname = request.POST.get('userName')
        print(f"Received nickname: {nickname}")

        if User.objects.filter(nickname=nickname).exists(): # 닉네임 조회 성공
            user = User.objects.get(nickname=nickname)

            request.session['nickname'] = user.nickname # 세션에 닉네임 저장

            if user.result_area == 'a': # 결과가 a인 사용자
                return render(request, 'main/mainLogin_a.html')
            elif user.result_area == 'b': # 결과가 b인 사용자
                return render(request, 'main/mainLogin_b.html')
            else:
                return JsonResponse({'message': '성향결과를 조회할 수 없습니다.'}, status=404)
        
        else: # 닉네임 조회 실패
            return render(request, 'login/login.html', {
                'error_message' : '성향검사를 통해 당신의 포레스트를 먼저 찾아주세요!'
            })
    else:
        return render(request, 'login/login.html')

    
# 로그아웃
def user_logout(request):
    if 'nickname' in request.session:
        del request.session['nickname'] # 'nickname' 세션 키 삭제
    #로그아웃 처리 추가
    return render(request, 'main/') # 로그아웃된 main페이지 렌더링