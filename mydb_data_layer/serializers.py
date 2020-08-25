from rest_framework import serializers

from mydb_data_layer import models


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Result
        fields = '__all__'

class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Search
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Address
        fields = '__all__'