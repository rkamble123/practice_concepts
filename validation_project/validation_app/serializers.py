from rest_framework import serializers
from .models import stu_model


class stu_serializer(serializers.Serializer):

    def start_with_r(data):
        if data[0].lower()!='r':
            raise serializers.ValidationError('Only Name Starting with R is Allowed')
        return data

    name = serializers.CharField(max_length=100,validators = [start_with_r])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)


    def create(self, validated_data):
        return stu_model.objects.create(**validated_data)


    # Field level validation

    def validate_roll(self,roll):
        if roll >= 200:
            raise serializers.ValidationError('Seat Full')
        return roll


    # Objec level Validation


    def validate(self,data):
        name_data=data.get('name')
        city_data = data.get('city')
        if name_data=='sahil' and city_data != 'vashi':
            raise serializers.ValidationError('City of Sahil Must Be Vashi')
        return data