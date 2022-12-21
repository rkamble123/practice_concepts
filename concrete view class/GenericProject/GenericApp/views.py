from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import StudentModel
from .serializers import StudentSerializer

# Create your views here.

class ListCreateStudent(ListCreateAPIView):
     queryset = StudentModel.objects.all()
     serializer_class = StudentSerializer 


class ReadUpdateDeleteStudent(RetrieveUpdateDestroyAPIView):
     queryset = StudentModel.objects.all()
     serializer_class = StudentSerializer





