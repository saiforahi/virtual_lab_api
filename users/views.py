import sys

from django.shortcuts import render
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from users.auth import EmailModelBackend
from users.models import User
from users.serializers import UserCreateSerializer, UserDetailSerializer
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.


class Login(APIView):
    permission_classes = (AllowAny,)

    def post(self,request):
        try:
            auth_user = EmailModelBackend.authenticate(User.objects.get(email=request.data.get('email')), email=request.data.get('email'),password=request.data.get('password'))
            if auth_user:
                refresh = RefreshToken.for_user(auth_user)
                response = {
                    'success': 'True',
                    'status code': status.HTTP_200_OK,
                    'message': 'Login successful',
                    'data':{'refresh':str(refresh),'access':str(refresh.access_token)}
                }
            else:
                response = {
                    'success': 'True',
                    'status code': status.HTTP_200_OK,
                    'message': 'Wrong Credentials',

                }
            return Response(response,status=status.HTTP_200_OK)
        except Exception as e:
            response = 'on line {}'.format(sys.exc_info()[-1].tb_lineno), str(e)
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class Register(APIView):
    permission_classes = (AllowAny,)

    def post(self,request):
        try:
            req_data = UserCreateSerializer(data=request.data)
            req_data.is_valid(raise_exception=True)
            user_email=req_data.create(req_data.validated_data)
            print(user_email)
            new_user=UserDetailSerializer(User.objects.get(email=user_email)).data
            response = {
                'success': 'True',
                'status code': status.HTTP_200_OK,
                'message': 'Registration completed',
                'data': new_user
            }
            return Response(response,status=status.HTTP_200_OK)
        except APIException as e:
            errors={}
            exception_detail=e.detail
            if exception_detail:
                for value in e.detail:
                    errors[value] = e.detail[value]
            else:
                errors.append(str(e))
            response = {
                'success': 'False',
                'status_code': status.HTTP_400_BAD_REQUEST,
                'message': 'Registraion failed',
                'errors':errors
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            response = 'on line {}'.format(sys.exc_info()[-1].tb_lineno), str(e)
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class Logout(APIView):
    permission_classes = (AllowAny,)

    def post(self,request):
        try:
            response = {
                'success': 'True',
                'status code': status.HTTP_200_OK,
                'message': 'Logout successful',
            }
            return Response(response,status=status.HTTP_200_OK)
        except Exception as e:
            response = 'on line {}'.format(sys.exc_info()[-1].tb_lineno), str(e)
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class UserDetails(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        try:
            user = UserDetailSerializer(request.user).data
            response = {
                'success': 'True',
                'status code': status.HTTP_200_OK,
                'message': 'User Details',
                'data':user
            }
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            response = 'on line {}'.format(sys.exc_info()[-1].tb_lineno), str(e)
            return Response(response, status=status.HTTP_400_BAD_REQUEST)