from django.urls import path
from .views import createview,createView,serialize,gnCreate

urlpatterns = [
    path('createview',createview,name='createview'),
    path('viewcl/',createView.as_view(),name='viewcl'),
    path('serialize/',serialize,name="serialize"),
    path('gnCreate/',gnCreate.as_view(),name = 'gnCreate')
]
