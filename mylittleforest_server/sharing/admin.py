from django.contrib import admin
from .models import Post_content, Comment, Scrap

admin.site.register(Post_content) #import한 클래스를 Admin 사이트에 등록
admin.site.register(Comment)
admin.site.register(Scrap)