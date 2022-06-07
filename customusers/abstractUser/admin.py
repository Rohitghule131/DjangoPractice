from django.contrib import admin
from abstractUser.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.

class UserAdmin(BaseUserAdmin):
    fieldsets = (
    (None, {'fields': ('email', 'password', )}),
      (('Personal info'), {'fields': ('first_name', 'last_name')}),
      (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                     'groups', 'user_permissions')}),
      (('Date'), {'fields': ('last_login', 'date_joined')}),
        (('user_info'), {'fields': ('name', 'phone_no')}),
    )
    add_fields = (
        (None, {
          'classes': ('wide', ),
          'fields': ('email', 'password1', 'password2'),
        }),
    )

    list_display = ['email', 'first_name', 'last_name', 'is_staff', "name", "phone_no"]
    search_fields = ['email','usename','first_name']
    ordering = ['email']

admin.site.register(User,UserAdmin)
  