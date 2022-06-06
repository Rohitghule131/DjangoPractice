from django.db import models

# Create your models here.

class Publications(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ['title']
    
    def __str__(self):
        return self.title

class Article(models.Model):
    headline = models.CharField(max_length=30)
    Publications = models.ManyToManyField(Publications)

    def __str__(self):
        return self.headline