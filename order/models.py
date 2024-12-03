from django.db import models
from product.models import Product
from django.contrib.auth.models import User

class Order(models.Model):
    address = models.CharField(max_length=255, verbose_name='адрес')
    created_at = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=100, verbose_name='номер телефона', default='87010000000')
    total = models.FloatField(default = 0) 
    
    class Meta:
        db_table = 'order'

    
class Payment(models.Model):
    card_number = models.CharField(max_length=100)
    Person_name = models.CharField(max_length=50)
    Expiry = models.CharField(max_length=50)
    cvv = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)  
    order = models.OneToOneField(Order, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'payment'




# Create your models here.
