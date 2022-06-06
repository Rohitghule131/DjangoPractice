from django import http
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from .form import contactForm
from .models import Contact
from .obj import contactclass
# from .serializer import SerializeContact
from .serializer import SerializeContact

def functionView(request, formscreen):
    formscreenn = formscreen
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['first_name'])
            return HttpResponse("submitted")
    else:
        form = contactForm()
        return render(request,formscreenn,{'form':form})
    # return HttpResponse("url seetings")

def serializeObj(request):
    fname = contactclass.first_name
    lname = contactclass.last_name
    contact = Contact(first_name=fname,last_name=lname)
    contact.save()
    serializer = SerializeContact(contactclass)

    # serializer.is_valid(raise_exception=True)
    # serializer.save()
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')


def funView(resquest):
    return HttpResponse("Im function")

class classView(APIView):

    def get(self,request):
        return HttpResponse("im class")
    