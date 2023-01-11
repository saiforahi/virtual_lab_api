from django.db import models


# Create your models here.

class TestBed(models.Model):
    name = models.CharField(max_length=255, verbose_name="Test Bed Name", null=False, blank=False, unique=True)
    specs = models.JSONField(default=dict, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        db_table = 'test_beds'
        verbose_name = 'Test Bed'
        verbose_name_plural = 'Test Beds'

    def __str__(self):
        return self.name


class WidgetType(models.Model):
    name = models.CharField(max_length=255, verbose_name="Widget Type Name", null=False, blank=False, unique=True)
    specs = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        db_table = 'widget_types'
        verbose_name = 'Widget Type'
        verbose_name_plural = 'Widget Types'

    def __str__(self):
        return self.name


class ToolType(models.Model):
    name = models.CharField(max_length=255, verbose_name="Tool Type Name", null=False, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        db_table = 'tool_types'
        verbose_name = 'Tool Type'
        verbose_name_plural = 'Tool Types'

    def __str__(self):
        return self.name


class Tool(models.Model):
    type = models.ForeignKey(ToolType, on_delete=models.CASCADE, null=False, blank=False,
                             error_messages={'null': 'Tool Type is required'})
    name = models.CharField(max_length=255, verbose_name="Tool Name", null=False, blank=False, unique=True)
    widget_type = models.ForeignKey(WidgetType, on_delete=models.SET(None), null=True, blank=True)
    user_values = models.JSONField(default=dict, null=True, blank=True)
    mqtt_data=models.JSONField(default=dict, null=True, blank=True)
    specs = models.JSONField(default=dict, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        db_table = 'tools'
        verbose_name = 'Tool'
        verbose_name_plural = 'Tools'

    def __str__(self):
        return self.name
