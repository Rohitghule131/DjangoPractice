from django.contrib import admin

from genericview.models import Person
from .models import Person
# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name']

admin.site.register(Person,PersonAdmin)
