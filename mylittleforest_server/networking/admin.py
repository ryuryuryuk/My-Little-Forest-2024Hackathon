from django.contrib import admin
from networking.models import Custom_group, Tag

admin.site.register(Custom_group) #import한 클래스를 Admin 사이트에 등록
admin.site.register(Tag)