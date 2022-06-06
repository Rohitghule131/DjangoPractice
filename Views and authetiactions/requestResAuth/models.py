from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    desc = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Cars(models.Model):
    person = models.ForeignKey(Person,on_delete=models.CASCADE)
    car_model = models.CharField(max_length=30)

    def __str__(self):
        return self.car_model

