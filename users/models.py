from django.db import models

# Create your models here.
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager

# Create your models here.
# from users.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    class GENDER(models.IntegerChoices):
        MALE = (0, 'MALE')
        FEMALE = (1, 'FEMALE')
        OTHER = (2, 'OTHER')

    first_name = models.CharField(verbose_name="First Name", max_length=150, blank=True)
    last_name = models.CharField(verbose_name='Last Name', max_length=150, blank=True)
    email = models.EmailField('Email', null=False, blank=False, unique=True,error_messages={'unique':'An user with this email already exists'})
    phone = models.CharField('Phone',max_length=11,unique=True,null=False,blank=False,error_messages={
        'unique':'An user with this phone number already exists'
    })
    age = models.IntegerField(max_length=150,blank=True, null=True)
    gender = models.IntegerField(choices=GENDER.choices, null=True, blank=True)
    usr_profile_pic = models.ImageField(upload_to='uploads/users/images/', blank=True, null=True)
    is_verified = models.BooleanField('verified', default=True, help_text='Designates whether this user is verified')
    is_notification = models.BooleanField('notification', default=False,help_text='User get Notification using Apps')
    is_message = models.BooleanField('message', default=False, help_text='User get mobile SMS')
    is_staff = models.BooleanField(
        'staff status',
        default=False,
        help_text='Designates whether the user can log into this admin site.',
    )
    is_active = models.BooleanField(
        'active',
        default=False,
        help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.',
    )
    fb_profile_link = models.TextField(verbose_name="Facebook Profile",max_length=1050,blank=True,null=True)
    twitter_profile_link = models.TextField(verbose_name="Twitter Profile",max_length=1050,blank=True,null=True)
    linkedin_profile_link = models.TextField(verbose_name="Linkedin Profile",max_length=1050,blank=True,null=True)
    date_joined = models.DateTimeField('date joined', auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(default=None, null=True, blank=True)
    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'auth_user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email

    def image_tag(self):
        from django.utils.html import escape
        return u'<img src="%s" />' % escape( "http://localhost:8000/".join(self.usr_profile_pic))
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True



class BillingInformation(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,blank=False,null=False)

