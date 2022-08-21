from email.policy import default
from importlib.metadata import requires
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from taggit.managers import TaggableManager
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey('Category' , on_delete=models.SET_NULL , null=True , blank=True)
    image = models.ImageField(upload_to='blog/' , default='blog/163529.jpg')
    tags = TaggableManager()

    def __str__(self) :
        return self.title

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"   



class Category(models.Model):
    name = models.CharField(max_length=225)   

    def __str__(self) :
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"    


class Comments(models.Model):
    user_id = models.IntegerField(default=1)
    post_id = models.IntegerField(default=1)
    email = models.EmailField()
    phone = models.IntegerField()
    text = models.TextField()
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.text)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"     



