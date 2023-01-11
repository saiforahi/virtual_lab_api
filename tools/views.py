import sys
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from tools.models import Tool, ToolType
from tools.serializers import ToolSerializer
from virtual_lab_api.helper import error_response, success_response


# Create your views here.

class ToolList(APIView):
    permission_classes = (AllowAny,)

    def get(self, request,type_name):
        try:
            toolType = ToolType.objects.get(name__iexact=type_name)
            tools=ToolSerializer(Tool.objects.filter(type=toolType),many=True).data
            response = {
                'success': True,
                'status_code': status.HTTP_200_OK,
                'message': type_name+' List',
                'data':tools
            }
            return Response(response, status=status.HTTP_200_OK)

        except ToolType.DoesNotExist as e:
            response = {
                'success': True,
                'status_code': status.HTTP_200_OK,
                'message': type_name+' List',
                'data': []
            }
            return Response(response, status=status.HTTP_200_OK)