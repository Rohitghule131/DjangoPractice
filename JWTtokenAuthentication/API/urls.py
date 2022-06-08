from sys import path_hooks
from django.urls import path
from API import views

urlpatterns = [
    path('hellov/',views.HelloView.as_view(),name='hellov'),

]
