from django.contrib import admin
from django.urls import path, include

from .views import ProjectManage,UploadDiagram,ArenaFeed

urlpatterns = [
    path("manage/", ProjectManage.as_view()),
    path("diagram/upload/",UploadDiagram.as_view()),
    path("arena/feed/",ArenaFeed.as_view())
    # path("create/", CreateProject.as_view()),
]

