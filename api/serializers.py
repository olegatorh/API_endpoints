from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from .models import *


class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = "__all__"


class DoctorSerializer(serializers.ModelSerializer):
    direction = PrimaryKeyRelatedField(many=True, queryset=Direction.objects.all())

    class Meta:
        model = Doctor
        fields = ['id', 'name', 'direction', 'slug', 'description', 'birthday', 'work_experience']
