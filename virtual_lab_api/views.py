import sys
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from virtual_lab_api.helper import error_response, success_response
from bangladesh import *

def redirect_view(request):
    # response = redirect('/nfc/admin/')
    response = redirect('/admin/')
    return response


class BangladeshData(APIView):
    permission_classes = (AllowAny,)
    def get(self,request):
        try:
            response = {
                "divisions": get_divisions()['divisions'],
                "districts": get_districts()['districts'],
                "upazilas": get_upazilas()['upazilas'],
                "postcodes": get_postcodes()['postcodes']
            }
            return Response(success_response(data=response, message='Bangladesh Geo data'),
                            status=status.HTTP_200_OK)
        except Exception as e:
            response = 'on line {}'.format(sys.exc_info()[-1].tb_lineno), str(e)
            return Response(error_response(errors=[response], message='Bangladesh Geo data failed'),
                            status=status.HTTP_400_BAD_REQUEST)