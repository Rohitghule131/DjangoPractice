from .models import Person
from rest_framework import serializers

class PersonSerialzer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    rollNo = serializers.IntegerField()
    desc = serializers.CharField(max_length=30)

    class Meta:
        model = Person
        fields = '__all__'
    
    def create(self, validated_data):
        return Person.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.rollNo = validated_data.get('rollNo',instance.rollNo)
        instance.desc = validated_data.get('desc',instance.desc)
        instance.save()
        return instance
    # def update(self, instance, validated_data):
    #     return Person.objects.update(instance, **validated_data)

    