from django.urls import path
from models2 import views as v

urlpatterns = [
    path('createPerson/<int:id>',v.createPerson.as_view(),name='createPerson'),
    path('permituser/',v.PermitView.as_view(),name='permituser'),
]
