import sys
from datetime import datetime

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from schedules.models import Schedule
from schedules.serializers import ScheduleSerializer
from virtual_lab_api.helper import error_response, success_response


# Create your views here.


class ScheduleList(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        try:
            schedules = ScheduleSerializer(Schedule.objects.all(), many=True).data
            return Response(success_response(data=schedules, message='Schedule List'),
                            status=status.HTTP_200_OK)
        except Exception as e:
            response = 'on line {}'.format(sys.exc_info()[-1].tb_lineno), str(e)
            return Response(error_response(errors=[response], message='Schedule List failed'),
                            status=status.HTTP_400_BAD_REQUEST)


class DateList(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        try:
            dates = Schedule.objects.filter(date__gte=datetime.today()).order_by('date').values_list('date',flat=True).distinct()

            return Response(success_response(data=dates, message='Date List'),
                            status=status.HTTP_200_OK)
        except Exception as e:
            response = 'on line {}'.format(sys.exc_info()[-1].tb_lineno), str(e)
            return Response(error_response(errors=[response], message='Schedule List failed'),
                            status=status.HTTP_400_BAD_REQUEST)


class TimeList(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        try:
            dates = ScheduleSerializer(Schedule.objects.order_by().values_list('date').distinct(), many=True).data
            return Response(success_response(data=dates, message='Date List'),
                            status=status.HTTP_200_OK)
        except Exception as e:
            response = 'on line {}'.format(sys.exc_info()[-1].tb_lineno), str(e)
            return Response(error_response(errors=[response], message='Schedule List failed'),
                            status=status.HTTP_400_BAD_REQUEST)