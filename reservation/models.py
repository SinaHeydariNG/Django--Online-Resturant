from django.db import models

# Create your models here.


class Reservation(models.Model):
    name = models.CharField(max_length=225)
    email = models.EmailField()
    phone = models.IntegerField()
    people = models.IntegerField()
    date = models.DateField()
    time = models.TimeField(auto_now_add=True)


    def __str__(self):
        return self.name
