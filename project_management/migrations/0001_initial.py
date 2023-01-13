# Generated by Django 4.1.1 on 2023-01-13 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tools', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.TextField(choices=[('DATE BOOKED', 'DATE BOOKED'), ('DRAFT', 'DRAFT'), ('PENDING', 'PENDING'), ('COMPLETED', 'COMPLETED')], default='DATE BOOKED')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
                'db_table': 'projects',
            },
        ),
        migrations.CreateModel(
            name='ProjectTool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_management.project')),
                ('tool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tools.tool')),
            ],
            options={
                'verbose_name': 'Project Tool',
                'verbose_name_plural': 'Project Tools',
                'db_table': 'project_tools',
            },
        ),
    ]
