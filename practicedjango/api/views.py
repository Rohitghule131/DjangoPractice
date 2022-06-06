import io

from django.shortcuts import render,HttpResponse
# from django.http import HTTPResponse
from .models import Person
from .serializer import PersonSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    per = Person.objects.get(first_name="Rohit")
    serializer = PersonSerializer(per)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')

@csrf_exempt
def setSerializer(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = PersonSerializer(pythondata)
        if serializer.is_valid():
            serializer.save()
            response_msg = {'msg':'data Inserted'}
            json_data = JSONRenderer().render(response_msg)
            return HttpResponse(json_data,content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        # return HttpResponse(json_data,content_type='application/json')

    
    