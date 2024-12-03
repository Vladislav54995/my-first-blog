from django.db import models
from product.models import Product
from order.models import Order
from django.contrib.auth import get_user_model

User = get_user_model()
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'cart'

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.RESTRICT)
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    amount = models.PositiveIntegerField(default=1)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True, related_name='cart_items')
    class Meta:
        db_table = 'cart_item'

# Create your models here.
