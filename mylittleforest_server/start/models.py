from django.db import models

class User(models.Model):

    user_id = models.AutoField(primary_key=True) #번호(pk)
    
    nickname = models.CharField(max_length=30, unique=True) #닉네임(unique)
    
    prefer = models.CharField(max_length=10, null=True, blank=True)  # 선호
    interest = models.CharField(max_length=10, null=True, blank=True)  # 관심사
    job = models.CharField(max_length=10, null=True, blank=True)  # 직업
    env = models.CharField(max_length=10, null=True, blank=True)  # 생활환경
    budget = models.CharField(max_length=10, null=True, blank=True)  # 예산
    fam = models.CharField(max_length=10, null=True, blank=True)  # 가족 수
    result_area = models.CharField(max_length=10, null=True, blank=True)  # 추천 지역

    # 문자열 표현을 위한 메서드
    def __str__(self):
        return self.nickname

