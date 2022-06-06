from django.shortcuts import render
from modelss.models import Person
from modelss.serializer import PersonSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
# Create your views here.

def serilizeJson(request):
    data = Person.objects.all()
    serialize = PersonSerializer(data,many=True)
    print(serialize.data)
    json_data = JSONRenderer().render(serialize.data)
    return HttpResponse(json_data,content_type='application/json')

class PersonList(GenericAPIView,ListModelMixin):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class PersonCreate(GenericAPIView,CreateModelMixin):
    queryset = Person
    serializer_class = PersonSerializer

    # def create(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class PersonRetrive(GenericAPIView,RetrieveModelMixin):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class PersonUpdate(GenericAPIView,UpdateModelMixin):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    
    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
class DeletePerson(GenericAPIView,DestroyModelMixin):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

def GetResponse(request,pk):
    try:
        
        per = Person.objects.get(id=pk)
        serializer = PersonSerializer(per)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')
    except BaseException as e:
        return HttpResponse("This data not available in database",e)
    

