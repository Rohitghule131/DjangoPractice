from unicodedata import name
from django.urls import path,include
from .views import classView, funView, functionView
from .views import serializeObj

urlpatterns = [
    path('',functionView,{'formscreen':'formScreen.html'},name='home'),
    path('sedata/',serializeObj,name='sedata'),
    path('funView/',funView,name='funView'),
    path('classView/',classView.as_view(),name='classView'),
]
