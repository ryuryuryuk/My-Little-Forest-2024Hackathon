from django.db import models

class Custom_group(models.Model):
    group_id = models.AutoField(primary_key=True)
    # 그룹 생성자(User.user_id 참조)
    constructor = models.ForeignKey(
        'start.User',  # start는 앱 이름, 'User'는 모델 이름
        on_delete=models.CASCADE,  # 삭제 정책
        related_name='custom_groups',  # 역참조 이름
        to_field='user_id'  # 참조할 필드 이름
    )
    image = models.ImageField(upload_to='group_images/')  # MEDIA_ROOT/group_images/ == /media/group_images
    group_name = models.CharField(max_length=30, unique=True)  # 그룹 이름
    description = models.TextField()  # 그룹 설명

    # 문자열 표현을 위한 메서드
    def __str__(self):
        return self.group_name

class Tags(models.Model):
    group_id = models.ForeignKey(
        'networking.Custom_group', 
        on_delete=models.CASCADE,
        related_name='tags',
        to_field='group_id'
    )
    tags = models.CharField(max_length=30)

    # 문자열 표현을 위한 메서드
    def __str__(self):
        return self.tags
