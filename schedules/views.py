import sys
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from schedules.models import Schedule
from schedules.serializers import ScheduleSerializer
from virtual_lab_api.helper import error_response, success_response


# Create your views here.


class ScheduleList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            schedules = ScheduleSerializer(Schedule.objects.all(), many=True).data
            return Response(success_response(data=schedules, message='Schedule List'),
                            status=status.HTTP_200_OK)
        except Exception as e:
            response = 'on line {}'.format(sys.exc_info()[-1].tb_lineno), str(e)
            return Response(error_response(errors=[response], message='Schedule List failed'),
                            status=status.HTTP_400_BAD_REQUEST)