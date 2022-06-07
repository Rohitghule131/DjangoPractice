from curses import meta
from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers
from abstractUser.models import User

class UserSrializer(serializers.Serializer):
    class Meta:
        model = User
        fields = '__all__'
        