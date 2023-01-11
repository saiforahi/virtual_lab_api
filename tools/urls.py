from django.contrib import admin
from django.urls import path, include

from .views import ToolList

urlpatterns = [
    path("list/<str:type_name>/", ToolList.as_view()),
]

