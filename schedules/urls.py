from django.contrib import admin
from django.urls import path, include

from .views import ScheduleList,DateList,TimeList

urlpatterns = [
    path("list/", ScheduleList.as_view()),
    path("list/dates/", DateList.as_view()),
    path("list/times/", TimeList.as_view()),
]

