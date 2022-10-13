from django.contrib import admin
from django.urls import path, include

from .views import ProjectManage

urlpatterns = [
    path("manage/", ProjectManage.as_view()),
]

