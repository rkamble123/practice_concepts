from rest_framework import serializers
from .models import User


class UserModelSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model = User
        fields =    ['username','email','password','password2']
        extra_kwargs = {
            'password':{'write_only':True}
        }

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError("Password And Confirm Password Doesn't Match.")
        return super().validate(attrs)

    
    def create(self,validate_data):
        return User.objects.create_user(**validate_data)