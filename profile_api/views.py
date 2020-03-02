from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloAPIView(APIView):
    """ Test APIView """
    def get(self, request, format = None):
        """ returns a list of APIView features """
        an_api_view = [
        'Uses HTTP methods as function (get,post,patch, put,delete)',
        'is similar to traditional django view',
        'is mapped to URLS'
        ]
        return Response({'message':"Hello!",'an_apiview' : an_api_view})
