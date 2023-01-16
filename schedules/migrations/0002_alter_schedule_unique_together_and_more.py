# Generated by Django 4.1.1 on 2023-01-16 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='schedule',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='end_time',
            field=models.TimeField(error_messages={'blank': 'Ending time can not be empty'}),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='start_time',
            field=models.TimeField(error_messages={'blank': 'Starting time can not be empty'}),
        ),
        migrations.AlterUniqueTogether(
            name='schedule',
            unique_together={('date', 'start_time', 'end_time')},
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='test_bed',
        ),
    ]