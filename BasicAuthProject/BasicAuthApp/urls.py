from django.urls import path
from . import views


urlpatterns = [
    path('UserApi/',views.UserApi.as_view()),
]