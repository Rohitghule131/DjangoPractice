
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('model/',include('modelsfields.urls')),
    path('models2/',include('models2.urls')),
    
]
