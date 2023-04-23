from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.utils.text import slugify
from django.db.models.signals import post_save

# Create your models here.


class product(models.Model):
    farmer = models.ForeignKey(User,related_name='farmer',on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50)
    PROcategory = models.ForeignKey('Category',on_delete=models.CASCADE)
    description = models.TextField(max_length = 1000)
    added = models.DateTimeField(auto_now=True)
    weight= models.DecimalField(max_digits=5, decimal_places=2)  
    prices = models.DecimalField(max_digits=5, decimal_places=2)
    PROimg = models.ImageField(upload_to = 'PROimg',blank=True,null=True)
    slug = models.SlugField(blank=True,null=True)

    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.product_name)
        super(product,self).save(*args, **kwargs)

    def __str__(self) :
        return self.product_name    
   
class Category(models.Model):
    name = models.CharField(max_length = 50)
    def __str__(self) :
        return self.name
