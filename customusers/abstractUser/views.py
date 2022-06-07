from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from abstractUser.models import User
from rest_framework.mixins import  CreateModelMixin
from abstractUser.serializer import UserSrializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
# Create your views here.

class CreateUser(GenericAPIView,CreateModelMixin):
    queryset = User
    serializer_class = UserSrializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]

    def post(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class AddUser(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]
    def post(self,request):
        data = request.body

        serializer = UserSrializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse("User is created ")
        else:
            return HttpResponse("user is nott created ")