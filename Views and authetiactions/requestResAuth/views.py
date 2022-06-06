from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import GenericAPIView
from requestResAuth.serializer import CarsSerializer, PersonSerilizer
from requestResAuth.models import Cars, Person
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin
from rest_framework.views import APIView
from rest_framework.authentication import BaseAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import BasicAuthentication

# Create your views here.

class Personlist(GenericAPIView,ListModelMixin):
    queryset = Person.objects.all()
    serializer_class = PersonSerilizer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class PersonCreate(GenericAPIView,CreateModelMixin):
    queryset = Person.objects.all()
    serializer_class = PersonSerilizer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class PersonRetrive(GenericAPIView,RetrieveModelMixin):
    queryset = Person.objects.all()
    serializer_class = PersonSerilizer

    def get(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

class AuthView(APIView):
    authentication_classes = [SessionAuthentication,BaseAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request,format=None):
        # token = Token.objects.create(user=...)
        # print(f'token created :- {token.key}')
        content = {
            'user':str(request.user),
            'auth':str(request.auth)
        }
        return Response(content)

class CarView(GenericAPIView,CreateModelMixin):

    queryset = Cars.objects.all()
    serializer_class = CarsSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class updataPerson(GenericAPIView,UpdateModelMixin):

    queryset = Person.objects.all()

    serializer_class = PersonSerilizer

    def post(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

class PermitView(APIView):
    
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request,id=None):
        if id:
            item = Person.objects.get(id=id)
            serializer = PersonSerilizer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = Person.objects.all()
        serializer = PersonSerilizer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    
    def post(self,request,id=None):
        serializer = PersonSerilizer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,id):
        person = Person.objects.get(id=id)
        serializer = PersonSerilizer(person,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return HttpResponse("Data is Not valid")
    
    def delete(self,request,id):
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponse("Deleted")

class ReadOnly(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self,request,id=None):
        if id:
            item = Person.objects.get(id=id)
            serializer = PersonSerilizer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = Person.objects.all()
        serializer = PersonSerilizer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    
    def post(self,request,id=None):
        serializer = PersonSerilizer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,id):
        person = Person.objects.get(id=id)
        serializer = PersonSerilizer(person,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return HttpResponse("Data is Not valid")
    
    def delete(self,request,id):
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponse("Deleted")