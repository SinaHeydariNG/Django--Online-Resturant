import email
from django.db import models

# Create your models here.



class MessageRegister(models.Model):
    name = models.CharField(max_length=225)
    phone = models.IntegerField()
    email = models.EmailField()
    message = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name



class About(models.Model):
    title = models.CharField(max_length=225)
    content = models.TextField()
    image = models.ImageField(upload_to='user/') 

    def __str__(self):
        return self.title
