from django.db import models

from django.db import models

class Custom_group(models.Model):

	group_id = models.AutoField(primary_key=True)
	# 그룹 생성자(User.user_id 참조)
	constructor = models.ForeingKey(
		'start.User', # start는 앱 이름, 'User'는 모델 이름
		on_delete=models.CASADE, # 삭제 정책
		related_name='custom_groups', # 역참조 이름
		to_field='user_id' # 참조할 필드 이름
	)
	image = models.ImageField(upload_to='업로드된 이미지가 저장될 경로') # 그룹 이미지
	group_name = models.CharField(max_length=30, unique=True) # 그룹 이름
	description = models.TextField() #그룹 설명
