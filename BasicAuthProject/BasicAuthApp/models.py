from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    # course_assigned = models.ManyToManyField(CourseModel,blank=True)
    created_date = models.DateTimeField(auto_now_add=True,blank=True)
    updated_date = models.DateTimeField(auto_now=True,blank=True)
    
        
