from django.http import JsonResponse
from rest_framework import status


def json_response(code=200, msg="", data=None):
    data_dict = {"code": code, "msg": msg, "data": data or {}}
    return JsonResponse(data=data_dict, status=status.HTTP_200_OK)
