from django.shortcuts import render
from django.views import View
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from django.contrib.auth import get_user_model
from .serializers import UserModelSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.


class UserApi(ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserModelSerializer
    # def get(self,request,format =None):
    #     return Response({'Msg' : 'You are in get of UserApi'})


