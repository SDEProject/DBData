from django.contrib import admin

# Register your models here.
from mydb_data_layer import models

admin.register(models.Result)
admin.register(models.Search)