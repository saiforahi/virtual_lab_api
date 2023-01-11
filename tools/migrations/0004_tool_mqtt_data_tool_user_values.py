# Generated by Django 4.1.1 on 2023-01-11 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0003_alter_widgettype_specs'),
    ]

    operations = [
        migrations.AddField(
            model_name='tool',
            name='mqtt_data',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AddField(
            model_name='tool',
            name='user_values',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
    ]