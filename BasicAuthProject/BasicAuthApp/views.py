from django.shortcuts import render
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import BasePermission,IsAuthenticated
from rest_framework.generics import ListAPIView,ListCreateAPIView
# Create your views here.

class UserApi(ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]