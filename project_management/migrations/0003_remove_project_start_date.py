# Generated by Django 4.1.1 on 2022-10-06 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("project_management", "0002_project_owner_projecttool"),
    ]

    operations = [
        migrations.RemoveField(model_name="project", name="start_date",),
    ]
