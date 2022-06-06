from django.contrib import admin
from .models import Person
# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    list_display = ['id','name','rollNo','desc']


admin.site.register(Person,PersonAdmin)