from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager


# Create your CustomUserManager here.

class CourseModel(models.Model):
    course_name = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True,blank=True)
    updated_date = models.DateTimeField(auto_now=True,blank=True)

    def __str__(self):
        return self.course_name
    

class TopicsModel(models.Model):
    course_name = models.ForeignKey(CourseModel,on_delete=models.CASCADE)
    topic_name = models.CharField(max_length=100)
    topic_url = models.URLField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True,blank=True)
    update_date = models.DateTimeField(auto_now=True,blank=True)


    def __str__(self):
        return f'{self.course_name} {self.topic_name}'



class CustomUserManager(BaseUserManager):

    def _create_user(self, email, password=None,password2=None,**extra_fields):
        if not email:
            raise ValueError("Email must be provided")
        if not password:
            raise ValueError('Password is not provided')

        user = self.model(
            email = self.normalize_email(email),
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self,email, password=None,password2=None, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(email,password, password2, **extra_fields)

    def create_superuser(self,email, password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',True)
        return self._create_user(email,password,**extra_fields)


# Create your User Model here.

class User(AbstractBaseUser,PermissionsMixin):

    # Abstractbaseuser has password, last_login, is_active by default
    username = models.CharField(unique=True,max_length=100)
    email = models.EmailField(db_index=True, unique=True, max_length=254)
    first_name = models.CharField(max_length=240)
    last_name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=50)
    address = models.CharField( max_length=250)
    created_date = models.DateTimeField(auto_now_add=True,blank=True)
    updated_date = models.DateTimeField(auto_now=True,blank=True)
    course_assigned = models.ManyToManyField(CourseModel,blank=True)

    is_staff = models.BooleanField(default=True) # must needed, otherwise you won't be able to loginto django-admin.
    is_active = models.BooleanField(default=True) # must needed, otherwise you won't be able to loginto django-admin.
    is_superuser = models.BooleanField(default=False) # this field we inherit from PermissionsMixin.

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
