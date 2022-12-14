from django.db import models

# Create your models here.

class stu_model (models.Model):
    name = models.CharField(max_length=100)
    roll = models.PositiveIntegerField()
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    