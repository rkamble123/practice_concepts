from django.contrib import admin
from .models import CourseModel,TopicsModel,User


# Register your models here.


# admin.site.register(User)

@admin.register(User)
class UserAdminModel(admin.ModelAdmin):
    list_display = ['username','is_staff','is_active']


@admin.register(CourseModel)
class AdminCourse(admin.ModelAdmin):
    list_display=['course_name']


@admin.register(TopicsModel)
class AdminTopics(admin.ModelAdmin):
    list_display=['course_name','topic_name']
