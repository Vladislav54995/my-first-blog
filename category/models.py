from django.db import models
from django.views.generic import ListView

class Category(models.Model):
    name = models.CharField(max_length=100,verbose_name='Наименование')
    image = models.ImageField(upload_to='category', null=True, blank=True)
    

    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'category'
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['name']
        




# Create your models here.
