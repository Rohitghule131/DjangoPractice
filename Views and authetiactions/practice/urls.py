from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('view.urls')),
    path('gn/',include('genericview.urls')),
    path('res/',include('requestResAuth.urls')),
]
