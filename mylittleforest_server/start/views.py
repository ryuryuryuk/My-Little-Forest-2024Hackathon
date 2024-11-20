from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
from .models import User #import .model.User

#starting 페이지
def starting(request):#기존 회원과 신규 회원을 구분
    return render(request, 'start/starting.html')


# 신규 회원 가입 과정
def startingName(request):#닉네임 입력
    #POSt 요청: 닉네임 입력 로직
    if request.method == 'POST':#닉네임을 입력하고 post요청을 하면 처리하는 로직
        nickname = request.POST.get('nickname')
        #동일 닉네임 존재 시
        if User.objects.filter(nickname=nickname).exists():
            return render(request, 'start/startingName.html', {
                'error_message': '이미 존재하는 닉네임입니다.' #에러메세지로 뎀플릿 전달
            })
        #동일 닉네임 존재하지 않을 시
        user = User.objects.create(nickname=nickname) #user: 해당 nickname이 저장된 행 전체(딕셔너리 형태)
        #세션에 닉네임 저장
        request.session['nickname'] = user.nickname
        return redirect('start:startingName2')
    #GET 요청: 닉네임 입력 페이지 렌더링
    return render(request, 'start/startingName.html')


def startingName2(request):#닉네임을 포함한 인사말
    #세션에 닉네임이 없을 시
    if not request.session.get('nickname'):
        return JsonResponse({'message':'세션에 닉네임이 없습니다.'}, status=400)
    #세션에 닉네임이 있을 시
    return render(request, 'start/startingName2.html')

def startingPrefer(request):
        return render(request, 'start/startingPrefer.html')

def startingInterest(request):
    if request.method == 'POST':
        prefer = request.POST.get('choice')
        nickname = request.session.get('nickname')
        try:
            user = User.objects.get(nickname=nickname)
            user.prefer = prefer #db에 prefer 저장
            user.save()
            return render(request, 'start/startingInterest.html');#db에 저장 후 interest 페이지 경로로 리다이렉트
        except User.DoesNotExist:
            return JsonResponse({'message': '사용자를 찾을 수 없습니다.'}, status=404)
    
    elif request.method == 'GET':    
        return render(request, 'start/startingInterest.html')


def startingJob(request):
    if request.method == 'POST':
        interest = request.POST.get('choice') 
        nickname = request.session.get('nickname')
        try:
            user = User.objects.get(nickname=nickname)
            user.interest = interest
            user.save()
            return render(request, 'start/startingJob.html');
        except User.DoesNotExist:
            return JsonResponse({'message': '사용자를 찾을 수 없습니다.'}, status=404)
    
    elif request.method == 'GET':    
        return render(request, 'start/startingJob.html')


def startingEnv(request):
    if request.method == 'POST':
        job = request.POST.get('choice')
        nickname = request.session.get('job')
        try:
            user = User.objects.get(nickname=nickname)
            user.job = job
            user.save()
            return render(request, 'start/startingEnv.html');
        except User.DoesNotExist:
            return JsonResponse({'message': '사용자를 찾을 수 없습니다.'}, status=404)
        
    elif request.method == 'GET':    
        return render(request, 'start/startingEnv.html')

def startingBudget(request):
    if request.method == 'POST':
        env = request.POST.get('choice')
        nickname = request.session.get('nickname')
        try:
            user = User.object.get(nickname=nickname)
            user.env = env
            user.save()
            return render(request, 'start/startingFam.html');
        except User.DoesNotExist:
            return JsonResponse({'message': '사용자를 찾을 수 없습니다.'}, status=404)
    elif request.method == 'GET':    
        return render(request, 'start/startingBudget.html')

def startingFam(request):
    if request.method == 'POST':
        budget = request.POST.get('choice')
        nickname = request.session.get('nickname')
        try:
            user = User.object.get(nickname=nickname)
            user.budget = budget
            return render(request, 'start/startingFam.html');
        except User.DoesNotExist:
            return JsonResponse({'message': '사용자를 찾을 수 없습니다.'}, status=404)
    elif request.method == 'GET':  
        return redirect(request, 'start:result')

#성향 결과 페이지 결정
def result(request):
    # 세션에서 닉네임 가져오기
    nickname = request.session.get('nickname')
    
    if not nickname:
        return JsonResponse({'message': '세션에 닉네임 정보가 없습니다.'}, status=400)

    try:
        # User 모델에서 닉네임으로 사용자 검색
        user = User.objects.get(nickname=nickname)

        # 사용자 성향 속성 가져오기
        attributes = [user.prefer, user.interest, user.job, user.env, user.budget, user.fam]  # 6개의 속성값
        count_a = attributes.count('a')
        count_b = attributes.count('b')

        # 결과 페이지 결정
        if count_a >= count_b:
            return render(request, 'start/startingResult_a.html', {'user': user})
        else:
            return render(request, 'start/startingResult_b.html', {'user': user})
        
    except User.DoesNotExist:
        return JsonResponse({'message': '사용자를 찾을 수 없습니다.'}, status=404)

