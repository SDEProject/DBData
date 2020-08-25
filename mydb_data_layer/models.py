from django.db import models

# Create your models here.
class Address(models.Model):
    city = models.CharField(max_length=100, null=True, blank=True)
    street = models.CharField(max_length=100, null=True, blank=True)
    number = models.CharField(max_length=100, null=True, blank=True)
    province = models.CharField(max_length=100, null=True, blank=True)


class Result(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    accommodation_type = models.CharField(max_length=100, null=True, blank=True)
    start_hour = models.CharField(max_length=100, null=True, blank=True)
    end_hour = models.CharField(max_length=100, null=True, blank=True)
    lat_1 = models.FloatField(null=True, blank=True)
    long_1 = models.FloatField(null=True, blank=True)
    lat_2 = models.FloatField(null=True, blank=True)
    long_2 = models.FloatField(null=True, blank=True)
    stars = models.IntegerField(null=True, blank=True)
    type = models.CharField(max_length=100, null=True, blank=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='results')


class Search(models.Model):
    type = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)