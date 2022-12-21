from django.db import models


# Create your models here.

class StudentApiModel(models.Model):
    name = models.CharField(max_length=100)
    roll = models.PositiveIntegerField()
    city = models.CharField(max_length=100)
    
    

