from django.urls import path
from . import views

urlpatterns = [
    
    path('LCStudentApi/', views.LCStudentApi.as_view(),name='LCStudentApi'),
    path('RUDStudentApi/<int:pk>', views.RUDStudentApi.as_view(),name='RUDStudentApi'),

]