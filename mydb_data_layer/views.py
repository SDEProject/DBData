from django.shortcuts import render
import django_filters
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, mixins

from mydb_data_layer import models, serializers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Create your views here.
class ResultViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.DestroyModelMixin, mixins.CreateModelMixin):
    queryset = models.Result.objects.all()
    serializer_class = serializers.ResultSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['name', 'accommodation_type', 'start_hour', 'end_hour', 'lat_1', 'long_1', 'lat_2', 'long_2',
                        'path_from', 'path_to', 'time', 'path_length', 'path_difficulty', 'shop_enum', 'stars', 'type', 'user_id']

class SearchViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.DestroyModelMixin, mixins.CreateModelMixin):
    queryset = models.Search.objects.all()
    serializer_class = serializers.SearchSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['subject', 'checkin', 'city', 'comune_from', 'comune_to', 'class_to', 'class_from', 'region',
                        'poi_activity_from', 'poi_activity_to', 'path_number', 'information', 'shop_enum', 'order',
                        'path_difficulty', 'info_equipment', 'time_period', 'type', 'ordinal']

class AddressViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.DestroyModelMixin, mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin):
    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['city', 'street', 'number', 'province']