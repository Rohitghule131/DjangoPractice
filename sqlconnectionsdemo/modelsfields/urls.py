# from django.contrib import admin
from django.urls import path,include
from .views import posthere
from .views import updatehere
from modelsfields import views
urlpatterns = [
    path('addData',posthere,name='addData'),
    path('upData/<int:pk>',updatehere,name='upData'),
    path('dataCreate/',views.postdata,name='dataCreate'),
    path('crdata/',views.createData.as_view(),name = 'crdata'),
]
