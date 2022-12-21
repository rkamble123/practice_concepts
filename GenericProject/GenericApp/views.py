from django.shortcuts import render
from django.views import View
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from .models import StudentModel
from .serializers import StudentSerializer

# Create your views here.

class LCStudentApi(GenericAPIView,ListModelMixin,CreateModelMixin):

    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)



class RUDStudentApi(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)






