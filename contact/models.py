from django.db import models

# Create your models here.
class message(models.Model):
    name = models.CharField(max_length=50)
    email = models.TextField(max_length=254)    
    messsage = models.TextField(max_length=300)
    def __str__(self):
        return self.name 