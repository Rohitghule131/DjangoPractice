from rest_framework import serializers
from .models import Contact

class SerializeContact(serializers.Serializer):
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)

    def create(self,validate_data):
        return Contact.objects.create(**validate_data)