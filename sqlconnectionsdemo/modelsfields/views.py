
import io
from django.http import HttpResponse
from django.shortcuts import render
from .models import Person
from datetime import datetime
from .serializer import PersonSerializer
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import (GenericAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView,RetrieveAPIView)

# Create your views here.

def posthere(request):
    first_name = 'rohit'
    last_name = 'ghule'
    date = datetime.now()
    person = Person(first_name=first_name,last_name=last_name,date=date)
    person.save()
    return HttpResponse("submitted")

def updatehere(request,pk):
    person = Person.objects.get(id=pk)
    print(person)
    person.last_name = "GHULE"
    person.date = datetime.now()
    person.save()
        
    return HttpResponse('submmited')

@csrf_exempt
def postdata(request):
    try:
        if request.method == 'POST':
            json_data = request.body
            print("one")
            data = io.BytesIO(json_data)
            print('two')
            print(data)
            pythondata = JSONParser().parse(data)
            print("three")
            print(pythondata)
            serializer = PersonSerializer(data = pythondata)
            print("Three")
            if serializer.is_valid():
                serializer.save()
                msg = {'ms':'data created'}
                json_render = JSONRenderer().render(msg)
                return HttpResponse(json_render,content_type='application/json')
        else:
            return HttpResponse("data is not created something went wrong")
    except BaseException:
        return HttpResponse("Some error is occured")

class createData(CreateAPIView):
    serializer_class = PersonSerializer

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return HttpResponse("HTTP-DATA/CREATED-201")

