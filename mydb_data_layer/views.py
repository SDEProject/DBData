from django.shortcuts import render
import django_filters
from rest_framework import viewsets, mixins

from mydb_data_layer import models, serializers

# Create your views here.
class ResultViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.DestroyModelMixin, mixins.CreateModelMixin):
    queryset = models.Result.objects.all()
    serializer_class = serializers.ResultSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['name', 'accommodation_type', 'start_hour', 'end_hour', 'lat_1', 'long_1', 'lat_2', 'long_2', 'stars', 'type']


class SearchViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.DestroyModelMixin, mixins.CreateModelMixin):
    queryset = models.Search.objects.all()
    serializer_class = serializers.SearchSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['type', 'date', 'city']


class AddressViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.DestroyModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin):
    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['city', 'street', 'number', 'province']