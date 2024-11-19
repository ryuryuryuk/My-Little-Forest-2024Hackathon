from django.contrib import admin
from start.models import User #models.py에서 정의한 User클래스 import

admin.site.register(User) #import한 클래스를 Admin 사이트에 등록