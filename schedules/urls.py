from django.contrib import admin
from django.urls import path, include

from .views import ScheduleList

urlpatterns = [
    path("list/", ScheduleList.as_view()),
]

