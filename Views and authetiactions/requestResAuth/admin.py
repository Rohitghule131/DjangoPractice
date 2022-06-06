from django.contrib import admin
from requestResAuth.models import Person
from requestResAuth.models import Cars
# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name','city','desc']

class PersonCarAdmin(admin.ModelAdmin):
    list_display = ['person','car_model']

admin.site.register(Cars,PersonCarAdmin)
admin.site.register(Person,PersonAdmin)
