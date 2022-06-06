
from rest_framework import serializers
from .models import Person
class PersonSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    email = serializers.EmailField()
    # class Meta:
    #     model = Person
    #     fields = ['first_name','last_name','email']
