from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.response import Response
from profile_api import serializers
from rest_framework import status
from profile_api.models import UserProfile
from profile_api.permissions import UpdateOwnProfile
from rest_framework.authentication import TokenAuthentication


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



class HelloViewSet(ViewSet):


    serializer_class = serializers.HelloSerializer
    def create(self,request):
        """create a new hello msg"""
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            msg = "Hello {}!".format(name)
            return Response({'message':msg})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST,
            )

    def list(self,request):
        """ return a hello msg """
        a_viewset = [
            "uses actions -LIST,CREATE,RETRIEVE, UPDATE, PARTIAL_UPDATE",
            'AUTOMATICALLY MAPS TO URLS USING ROUTERS',
            'MORE FUNCTIONALITY'
        ]
        return Response({'message' : 'hello','a_viewset' : a_viewset})


    def retrieve(self, request, pk = None):
        return Response({"HTTP-method" :"GET"})

    def update(self,request,pk = None):
        return Response({"HTTP-method": "PUT"})

    def partial_update(self,request,pk = None):
        return Response({"HTTP-method": "PATCH"})

    def destroy(self,request,pk = None):
        return Response({"HTTP-method": "DELETE"})


class UserProfileViewSet(ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)
