from django.contrib import admin
from .models import StudentApiModel

# Register your models here.

# admin.site.register(StudentApiModel)

@admin.register(StudentApiModel)
class AdminStudentModel(admin.ModelAdmin):
    list_display = ['id','name','roll','city']