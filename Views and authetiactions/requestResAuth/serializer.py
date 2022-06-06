from rest_framework import serializers
from requestResAuth.models import Cars, Person

class PersonSerilizer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    city = serializers.CharField(max_length=30)
    desc = serializers.CharField(max_length=30)

    def create(self, validated_data):
        return Person.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()
        return instance

class CarsSerializer(serializers.Serializer):
    person = serializers.CharField(max_length=30)
    car_model = serializers.CharField(max_length=30)

    def create(self,validated_data):
        return Cars.objects.create(**validated_data)
