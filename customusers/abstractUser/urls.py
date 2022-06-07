from django.urls import path
from abstractUser import views as v
urlpatterns = [
    path('ucreate/',v.CreateUser.as_view(),name='ucreate'),
    path('adduser/',v.AddUser.as_view(),name="adduser"),
]