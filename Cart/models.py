from django.db import models
from dashboard.models import product
from django.contrib.auth.models import User

# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE,null=True)
    full_name = models.CharField(max_length=50)
    credit_card_name = models.CharField(max_length=50)    
    credit_card_number= models.IntegerField()
    expiration_date = models.DateTimeField()
    ccv = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order,related_name= 'items', on_delete=models.CASCADE)
    product = models.ForeignKey(product,related_name= 'items', on_delete=models.CASCADE)
    Price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.IntegerField(default=1)
    

  