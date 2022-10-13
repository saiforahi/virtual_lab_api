import sys

from django.contrib.auth.models import Group
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.validators import UniqueValidator

import users.models
from users.models import User

class UserDetailSerializer(serializers.ModelSerializer):
    groups = serializers.SerializerMethodField()

    def get_groups(self, obj):
        group_names=[]
        for g in obj.groups.all():
            group_names.append(g.name)
        # return [group.name for group in obj.groups]
        return group_names

    class Meta:
        model=User
        fields = ('id', 'first_name', 'last_name', 'usr_profile_pic', 'email', 'phone','groups')


class UserCreateSerializer(serializers.Serializer):
    email = serializers.CharField(required=True,error_messages={'required':"Email is required"},validators=[UniqueValidator(queryset=User.objects.all(),message='A user is already registered with this email.')])
    first_name = serializers.CharField(required=True,max_length=255)
    last_name = serializers.CharField(allow_null=False,allow_blank=True,max_length=255)
    password = serializers.CharField(required=True,min_length=8,max_length=100,allow_blank=False,allow_null=False)
    phone = serializers.CharField(required=True, min_length=11, max_length=20, allow_null=False, allow_blank=False)
    usr_profile_pic = serializers.ImageField(required=False, allow_empty_file=True)

    def create(self, validated_data):
        try:
            user = User.objects.create(email=validated_data['email'],first_name=validated_data['first_name'],last_name=validated_data['last_name'],phone=validated_data['phone'])
            user.set_password(validated_data['password'])
            if 'usr_profile_pic' in validated_data:
                user.usr_profile_pic = validated_data['usr_profile_pic']
            user.save()
            user_group = Group.objects.get(name='User')
            user_group.user_set.add(user)

            return user
        except Exception as e:
            response = 'on line {}'.format(sys.exc_info()[-1].tb_lineno), str(e)
            return response