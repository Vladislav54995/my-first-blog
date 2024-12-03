from django.db import models
from category.models import Category 

class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    image = models.ImageField(upload_to='products', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'product'
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
