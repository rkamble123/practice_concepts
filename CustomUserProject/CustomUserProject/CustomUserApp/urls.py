from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.UserApi.as_view(),name='UserApi'),
    path("auth/",include('rest_framework.urls',namespace='rest_framework')),
]