# Generated by Django 4.1.1 on 2023-01-13 09:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tooltype',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='tooltype',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
