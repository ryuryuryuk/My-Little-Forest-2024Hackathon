from django.urls import path
from . import views

app_name = "sharing"

urlpatterns = [
    path('',views.sharingContents2, name='sharingContents2'),
    path('writeContents/',views.writeContents, name='writeContents'),
    path('writeContents_logic/',views.writeContents_logic, name='writeContents_logic'),

    # path('mycontents/',views.mycontents, name='mycontents'),
    # path('sharingContents/',views.sharingContents, name='sharingContents'),
    # path('postPage/',views.postPage, name='postPage'),
    # path('press_like/',views.press_like, name='press_like'),
    # path('press_scrap/',views.press_scrap, name='press_scrap'),
    # path('save_comment/', views.save_comment, name='save_comment')
]