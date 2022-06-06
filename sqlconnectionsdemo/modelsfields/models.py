from django.db import models
from datetime import datetime
# Create your models here.

class Person(models.Model):
    select_city = (
        ('mi','mumbai'),
        ('dl','delhi'),
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    
    # date = models.DateTimeField(auto_now=False,auto_created=False,auto_now_add=False)
