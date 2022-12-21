from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import StudentApiModel
from .serializers import StudentApiSerializer
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt 

# Create your views here.


@api_view(['GET','POST','PUT','PATCH','DELETE'])
def StudentApi(request,pk = None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            stu_data = StudentApiModel.objects.get(id=id)
            serializer = StudentApiSerializer(stu_data)
            return Response(serializer.data)
        stus_data = StudentApiModel.objects.all()
        serializer = StudentApiSerializer(stus_data,many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = StudentApiSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Crated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    if request.method == "PUT":
        id = pk
        stu_data = StudentApiModel.objects.get(id=id)
        serializer = StudentApiSerializer(stu_data,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Msg":"Data Updated Succesfully"},status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    if request.method == "PATCH":
        id = pk
        stu_data = StudentApiModel.objects.get(id=id)
        serializer = StudentApiSerializer(stu_data,data = request.data,partial =True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Msg":"Data Updated Succesfully"},status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    if request.method == "DELETE":
        id = pk
        stu_data = StudentApiModel.objects.get(id=id)
        stu_data.delete()
        return Response({"Msg":"Data Deleted Succesfully"},status=status.HTTP_202_ACCEPTED)

