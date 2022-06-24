from rest_framework import serializers
from .models import *


class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = "__all__"


class DoctorSerializer(serializers.ModelSerializer):
    direction = DirectionSerializer(many=True)

    class Meta:
        model = Doctor
        fields = ['id', 'name', 'slug', 'direction', 'description', 'birthday', 'work_experience']


