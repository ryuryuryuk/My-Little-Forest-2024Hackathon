from django.urls import path
from . import views
from django.conf.urls.static import static

app_name = "sharing"

urlpatterns = [
    path('',views.sharingContents, name='sharingContents'),
    path('post/<int:pk>/', views.postpage, name='postpage'),  # 게시글 상세 페이지
    path('writeContents/',views.get_writeContents, name='writeContents'),
    path('writeContents_logic/', views.writeContents_logic, name='writeContents_logic'),
    path('myContents/',views.myContents, name='myContents'),

    # path('sharingContents/',views.sharingContents, name='sharingContents'),
    # path('postPage/',views.postPage, name='postPage'),
    # path('press_like/',views.press_like, name='press_like'),
    # path('press_scrap/',views.press_scrap, name='press_scrap'),
    # path('save_comment/', views.save_comment, name='save_comment')
]