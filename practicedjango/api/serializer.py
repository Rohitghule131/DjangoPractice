from rest_framework import serializers
from .models import Person
class PersonSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    desc = serializers.CharField(max_length=30)

    def creat(validate_data):
        return Person.objects.create(**validate_data)