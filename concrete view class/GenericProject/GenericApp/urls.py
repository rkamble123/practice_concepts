from django.urls import path
from . import views

urlpatterns = [
    
    path('ListCreateStudent/', views.ListCreateStudent.as_view(),name='ListCreateStudent'),
    path('ReadUpdateDeleteStudent/<int:pk>', views.ReadUpdateDeleteStudent.as_view(),name='ReadUpdateDeleteStudent'),
    # path('liststudent/', views.liststudent.as_view(),name='liststudent'),


]