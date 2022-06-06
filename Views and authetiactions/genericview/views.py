from webbrowser import get
from django import http
from django.http import HttpResponse
from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from genericview.serializer import PersonSerialzer
from genericview.models import Person
import io
from rest_framework.parsers import JSONParser
from rest_framework import permissions
from rest_framework.authentication import BasicAuthentication

# Create your views here.

def createview(requests):
    if requests.method == 'POST':
        fname  = requests.POST.get('fname')
        lname  = requests.POST.get('lname')
        person = Person(first_name=fname,last_name=lname)
        person.save()
        return HttpResponse("submmited")
    else:
        return render(requests,'PersonForm.html')
class createView(APIView):
    def get(self,request):
        return render(request,'PersonForm.html')
    def post(self,request):
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        if (fname==' ' or lname==' ')or(fname=='' or lname==''):
            return HttpResponse(request,'PersonForm.html',{'invalid':''})
        person = Person(first_name=fname,last_name=lname)
        person.save()
        return render(request,'PersonForm.html')
    
# class UpdatePost(UpdateAPIView):

#     def __init__(self):
def serialize(request):
    data = Person.objects.get(first_name='affan')
    print(data)
    serializer = PersonSerialzer(data,many=False)
    print(serializer.data)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')

class gnCreate(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request):
        data = io.BytesIO(request.body)
        parse_json = JSONParser().parse(data)
        serialize = PersonSerialzer(data= parse_json)
        if serialize.is_valid():
            serialize.save()
            return HttpResponse('data created')
        else:
            return HttpResponse('data is not valid')

    def get(self,request):
        return render(request,'PersonForm.html')