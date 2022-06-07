from django.contrib import admin

from api.models import UserAccount

# Register your models here.

class UserAccountAdmin(admin.ModelAdmin):

    list_display = ('email', 'name', 'phone', 'is_staff',  'is_superuser')

admin.site.register(UserAccount,UserAccountAdmin)

# admin.site.register(UserAccount)