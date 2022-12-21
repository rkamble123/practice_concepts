from django.urls import path
from . import views


urlpatterns = [
    path('StudentApi',views.StudentApi.as_view(),name='StudentApi'),
    path('StudentApi/<int:pk>',views.StudentApi.as_view(),name='StudentApi'),

]