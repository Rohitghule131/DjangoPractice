from django.urls import path
import modelss.views as view

urlpatterns = [
    path('',view.serilizeJson,name='serializeJSON'),
    path('listP/',view.PersonList.as_view(),name='listP'),
    path('crP/',view.PersonCreate.as_view(),name='crP'),
    # path('rtP/<str:pk>',view.PersonRetrive.as_view(),name='rtP'),
    # path('upP/<int:pk>',view.PersonUpdate.as_view(),name='upP'),
    path('delP/<int:pk>',view.DeletePerson.as_view(),name='delP'),
    path('getP/<int:pk>',view.GetResponse,name='getP'),
]
