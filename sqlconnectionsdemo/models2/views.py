from functools import partial
from re import S
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Person
from .serializer import PersonSerialzer
from rest_framework import status
from django.shortcuts import get_list_or_404
from rest_framework.authentication import BasicAuthentication
from rest_framework import permissions
# Create your views here.
class createPerson(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self,request,id=None):
        if id:
            item = Person.objects.get(id=id)
            serializer = PersonSerialzer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = Person.objects.all()
        serializer = PersonSerialzer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    
    def post(self,request,id=None):
        serializer = PersonSerialzer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,id):
        person = Person.objects.get(id=id)
        serializer = PersonSerialzer(person,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return HttpResponse("Data is Not valid")
    
    def delete(self,request,id):
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponse("Deleted")

class PermitView(APIView):
    
    authentication_classes = [BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request,id=None):
        if id:
            item = Person.objects.get(id=id)
            serializer = PersonSerialzer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = Person.objects.all()
        serializer = PersonSerialzer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    
    def post(self,request,id=None):
        serializer = PersonSerialzer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,id):
        person = Person.objects.get(id=id)
        serializer = PersonSerialzer(person,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return HttpResponse("Data is Not valid")
    
    def delete(self,request,id):
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponse("Deleted")