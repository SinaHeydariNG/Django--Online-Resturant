from pyexpat import model
from django.db import models
from django.utils.text import slugify

# Create your models here.


class Meals(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField()
    price = models.DecimalField(max_digits=6,decimal_places=2)
    prepration_time = models.IntegerField()
    image = models.ImageField(upload_to='meals/')
    slug = models.SlugField(blank=True,null=True)
    category = models.ForeignKey("Category" , on_delete=models.SET_NULL , null=True , blank=True)
    
    class Meta:
        verbose_name = "Meal"
        verbose_name_plural = "Meals"


    def save(self , *args , **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(Meals , self).save(*args , **kwargs)    

    def __str__(self) -> str:
        return self.name


class Category(models.Model):   
    name = models.CharField(max_length=225)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self) :
        return self.name    