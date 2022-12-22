from django.shortcuts import render
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
# Create your views here.

class UserApi(ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = RegisterSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

class UserRCDApi(RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = RegisterSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]