from django.contrib import admin
from newconnection import models

# Register your models here.

class PublicationsAdmin(admin.ModelAdmin):
    list_display = ['title']



class ArticleAdmin(admin.ModelAdmin):
    list_display = ['headline','get_article']

    def get_article(self,obj):
        return obj.Publications.all()

admin.site.register(models.Publications,PublicationsAdmin)
admin.site.register(models.Article,ArticleAdmin)