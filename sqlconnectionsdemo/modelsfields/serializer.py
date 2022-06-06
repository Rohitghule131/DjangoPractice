from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    # date = serializers.DateTimeField()

    def create(self, validated_data):
        return Person.objects.create(**validated_data)