from django.db import models

# Create your models here.



class SiteDetails(models.Model):

    title = models.CharField(max_length=225)
    email = models.EmailField()
    location = models.CharField(max_length=225)
    copyright = models.CharField(max_length=225)
    phone = models.CharField(max_length=225 , default="0933872949")


    def __str__(self):
        return "YOUR SITE DETAILS"
