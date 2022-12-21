from django.contrib import admin
from .models import StudentModel

# Register your models here.

@admin.register(StudentModel)
class StudenAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll','city']


