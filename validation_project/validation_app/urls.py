from django.urls import path
from . import views


urlpatterns = [
    path('stu_api',views.stu_api.as_view()),
]