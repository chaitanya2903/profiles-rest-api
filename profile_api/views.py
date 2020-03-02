from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from profile_api import serializers
from rest_framework import status

class HelloAPIView(APIView):
    """ Test APIView """
    serializer_class  = serializers.HelloSerializer
    def get(self, request, format = None):
        """ returns a list of APIView features """
        an_api_view = [
        'Uses HTTP methods as function (get,post,patch, put,delete)',
        'is similar to traditional django view',
        'is mapped to URLS'
        ]
        return Response({'message':"Hello!",'an_apiview' : an_api_view})

    def post(self,request):
        """ create a hello message with name"""
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            msg = "Hello {}".format(name)
            return Response({'message':msg})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST,
            )

    def put(self,request,pk = None):
        """ Handle updating an object """
        return Response({"method": 'PUT'})

    def patch(self,request, pk = None):
        """ handle a partial update of an object """
        return Response({"method" : 'PATCH'})

    def delete(self,request,pk = None):
        """ delete an object """
        return Response({"method" : "DELETE"})
        
