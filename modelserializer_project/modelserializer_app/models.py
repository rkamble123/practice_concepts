from django.db import models

# Create your models here.


class UserModel(models.Model):

    name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    email = models.EmailField()
    create_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    update_date = models.DateField(blank=True,null=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name