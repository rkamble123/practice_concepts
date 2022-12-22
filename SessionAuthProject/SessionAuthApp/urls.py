from django.urls import path,include
from . import views

urlpatterns = [
    path('UserApi/',views.UserApi.as_view()),
    path('UserRCDApi/<int:pk>',views.UserRCDApi.as_view()),
    path('auth/',include('rest_framework.urls',namespace = 'rest_framework')),

]
