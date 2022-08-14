from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Meals)
admin.site.register(models.Category)
