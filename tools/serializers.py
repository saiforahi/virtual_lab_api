from rest_framework import serializers
from tools.models import Tool, ToolType, WidgetType


class WidgetTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=WidgetType
        # fields = "__all__"
        exclude = ('created_at', 'updated_at')


class ToolTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model=ToolType
        # fields = "__all__"
        exclude = ('created_at','updated_at')


class ToolSerializer(serializers.ModelSerializer):
    type = ToolTypeSerializer()
    widget_type = WidgetTypeSerializer()

    class Meta:
        model=Tool
        # fields = "__all__"
        exclude = ('created_at', 'updated_at')


