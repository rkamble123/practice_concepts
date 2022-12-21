from rest_framework import serializers
from .models import StudentApiModel

class StudentApiSerializer(serializers.ModelSerializer):
     class Meta:
        model = StudentApiModel
        fields = ['id','name','roll','city']