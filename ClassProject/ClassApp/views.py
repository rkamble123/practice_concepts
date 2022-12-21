from django.shortcuts import render
from rest_framework.views import APIView
from .models import StudentApiModel
from .serializers import StudentApiSerializer
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt 

# Create your views here.



class StudentApi(APIView):


    def get(self,request,pk=None,format=None):
        id = pk
        if id is not None:
            stu_data = StudentApiModel.objects.get(id=id)
            serializer = StudentApiSerializer(stu_data)
            return Response(serializer.data)
        stus_data = StudentApiModel.objects.all()
        serializer = StudentApiSerializer(stus_data,many=True)
        return Response(serializer.data)


    def post(self,request,format=None):

        serializer = StudentApiSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Crated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None,format=None):
        id = pk
        stu_data = StudentApiModel.objects.get(id=id)
        serializer = StudentApiSerializer(stu_data,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Msg":"Complete Data Updated"},status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def patch(self,request,pk=None,format=None):
        id = pk
        stu_data = StudentApiModel.objects.get(id=id)
        serializer = StudentApiSerializer(stu_data,data = request.data,partial =True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Msg":"Partial Data Updated"},status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,pk=None,format=None):
        id = pk
        stu_data = StudentApiModel.objects.get(id=id)
        stu_data.delete()
        return Response({"Msg":"Data Deleted Succesfully"},status=status.HTTP_202_ACCEPTED)

