# Generated by Django 4.1.1 on 2023-01-22 17:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='Last Name')),
                ('email', models.EmailField(error_messages={'unique': 'An user with this email already exists'}, max_length=254, unique=True, verbose_name='Email')),
                ('phone', models.CharField(error_messages={'unique': 'An user with this phone number already exists'}, max_length=11, unique=True, verbose_name='Phone')),
                ('age', models.IntegerField(blank=True, null=True)),
                ('gender', models.IntegerField(blank=True, choices=[(0, 'MALE'), (1, 'FEMALE'), (2, 'OTHER')], null=True)),
                ('usr_profile_pic', models.ImageField(blank=True, null=True, upload_to='uploads/users/images/')),
                ('is_verified', models.BooleanField(default=True, help_text='Designates whether this user is verified', verbose_name='verified')),
                ('is_notification', models.BooleanField(default=False, help_text='User get Notification using Apps', verbose_name='notification')),
                ('is_message', models.BooleanField(default=False, help_text='User get mobile SMS', verbose_name='message')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=False, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('fb_profile_link', models.TextField(blank=True, max_length=1050, null=True, verbose_name='Facebook Profile')),
                ('twitter_profile_link', models.TextField(blank=True, max_length=1050, null=True, verbose_name='Twitter Profile')),
                ('linkedin_profile_link', models.TextField(blank=True, max_length=1050, null=True, verbose_name='Linkedin Profile')),
                ('date_joined', models.DateTimeField(auto_now=True, verbose_name='date joined')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'db_table': 'auth_user',
            },
        ),
        migrations.CreateModel(
            name='BillingInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
