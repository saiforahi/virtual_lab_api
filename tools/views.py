import json
import sys
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from tools.helper import on_connect, on_publish
from tools.models import Tool, ToolType
from tools.serializers import ToolSerializer
import paho.mqtt.client as paho


# Create your views here.

class ToolList(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, type_name):
        try:
            toolType = ToolType.objects.get(name__iexact=type_name)
            tools = ToolSerializer(Tool.objects.filter(type=toolType), many=True).data
            response = {
                'success': True,
                'status_code': status.HTTP_200_OK,
                'message': type_name + ' List',
                'data': tools
            }
            return Response(response, status=status.HTTP_200_OK)

        except ToolType.DoesNotExist as e:
            response = {
                'success': True,
                'status_code': status.HTTP_200_OK,
                'message': type_name + ' List',
                'data': []
            }
            return Response(response, status=status.HTTP_200_OK)


class TestMQTT(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        try:
            client = paho.Client(client_id="bveuwiyr923rkh2nsjugbjbjh4o", userdata=None, protocol=paho.MQTTv5)
            client.on_connect = on_connect
            client.on_publish = on_publish
            client.connect("broker.hivemq.com", 1883)
            client.loop_start()
            client.publish(topic="VHL/SUB", payload="moisture_sensor_1:on_water", qos=2)
            # client.loop_stop()
            return Response('message sent')
        except Exception as e:

            print(str(e))
            return Response(str(e))


class MQTTPublish(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            print(request.data['payload'])
            client = paho.Client(client_id="bveuwiyr923rkh2nsjugbjbjh4o", userdata=None, protocol=paho.MQTTv5)
            client.on_connect = on_connect
            client.on_publish = on_publish
            client.connect("broker.hivemq.com", 1883)
            client.loop_start()
            client.publish(topic="VHL/SUB", payload=request.data.get("payload"), qos=2)
            # client.loop_stop()
            response = {
                'success': True,
                'status_code': status.HTTP_200_OK,
                'message': "Message sent"
            }
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            print(str(e))
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
