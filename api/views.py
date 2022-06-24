from rest_framework.filters import OrderingFilter
from .serializers import DoctorSerializer, DirectionSerializer
from rest_framework import viewsets
from .models import Doctor, Direction
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend


class DoctorFilter(filters.FilterSet):
    min_work_experience = filters.NumberFilter(field_name='work_experience', lookup_expr='gte')
    max_work_experience = filters.NumberFilter(field_name='work_experience', lookup_expr='lte')

    class Meta:
        model = Doctor
        fields = ['direction', 'max_work_experience', 'min_work_experience']


class DoctorView(viewsets.ModelViewSet):
    queryset = Doctor.objects.all().order_by('name', 'id')
    serializer_class = DoctorSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['work_experience']
    filterset_class = DoctorFilter


class DirectionView(viewsets.ModelViewSet):
    serializer_class = DirectionSerializer
    queryset = Direction.objects.all()
