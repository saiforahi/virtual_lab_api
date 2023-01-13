import sys

from django.shortcuts import render
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from project_management.models import Project
from project_management.serializers import ProjectSerializer
from virtual_lab_api.helper import error_response, success_response


# Create your views here.

class ProjectManage(APIView):
    # authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self,request):
        try:
            request.data['owner']=request.user.id
            serializer=ProjectSerializer(data=request.data)
            print(request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(success_response(data=serializer.data, message='Project created!',status_code=status.HTTP_201_CREATED),status=status.HTTP_201_CREATED)

        except APIException as e:
            return Response(error_response(errors=e.detail, message='Project creation failed'), status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            response = 'on line {}'.format(sys.exc_info()[-1].tb_lineno), str(e)
            return Response(error_response(errors=[response],message='Project creation failed'), status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def get(self,request):
        try:
            projects = ProjectSerializer(Project.objects.filter(owner=request.user),many=True).data
            return Response(success_response(data=projects, message='Project List'),
                        status=status.HTTP_200_OK)
        except Exception as e:
            response = 'on line {}'.format(sys.exc_info()[-1].tb_lineno), str(e)
            return Response(error_response(errors=[response], message='Project List failed'),
                        status=status.HTTP_400_BAD_REQUEST)


class UploadDiagram(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self,request):
        try:
            diagramFile=request.FILES.get('diagram', False)
            if bool(diagramFile) == True and request.data.get('project'):
                project=Project.objects.get(pk=request.data.get('project'))
                project.diagram=diagramFile
                project.save()
                return Response(success_response(data=ProjectSerializer(project,many=False).data, message='Project Data'),
                                status=status.HTTP_200_OK)
            else:
                return Response(error_response(errors=[], message='Project Diagram upload failed'),
                                status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            response = 'on line {}'.format(sys.exc_info()[-1].tb_lineno), str(e)
            return Response(error_response(errors=[response], message='Project List failed'),
                        status=status.HTTP_400_BAD_REQUEST)