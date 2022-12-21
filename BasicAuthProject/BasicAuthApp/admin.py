from django.contrib import admin
from django.contrib.auth.models import User
# Register your models here.

@admin.register(User)
class AdminCourse(admin.ModelAdmin):
    list_display=['username','is_staff','is_active']