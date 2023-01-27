from django.contrib import admin
from django.urls import path, include

from .views import ToolList,TestMQTT,MQTTPublish

urlpatterns = [
    path("list/<str:type_name>/", ToolList.as_view()),
    path("mqtt/test/",TestMQTT.as_view()),
    path("mqtt/publish/",MQTTPublish.as_view()),
]

