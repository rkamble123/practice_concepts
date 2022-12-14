from rest_framework import serializers
from .models import UserModel

class user_api(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = ['name','user_name','email','create_date','update_date','password']