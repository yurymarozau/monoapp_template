from django.db import connections
from django.http import JsonResponse
from rest_framework import permissions, views


class ApiInfo(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, *args, **kwargs):
        api_info = {
            'current_version': 'v1',
            'supported_versions': ['v1', ], }
        return JsonResponse(api_info)


class HealthCheck(views.APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, *args, **kwargs):
        connections['default'].cursor()
        return JsonResponse({})
