from django.db import models

class Custom_group(models.Model):
    group_id = models.AutoField(primary_key=True)
    constructor = models.CharField(max_length=30)
    image = models.ImageField(upload_to='group_images/')  # MEDIA_ROOT/group_images/ == /media/group_images
    group_name = models.CharField(max_length=30)  # 그룹 이름
    description = models.TextField()  # 그룹 설명

    # 문자열 표현을 위한 메서드
    def __str__(self):
        return self.group_name

class Tag(models.Model):
    group_name = models.CharField(max_length=30, null=True)
    tag = models.CharField(max_length=30, null=True)

    # 문자열 표현을 위한 메서드
    def __str__(self):
        return self.tag
