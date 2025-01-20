from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100 ,default='empety' , verbose_name='Title')  #CHANGED THE NAME TO TITLE verbose_name='Title'
    content = models.TextField(null=True , blank=True) 
    price = models.DecimalField(max_digits=10, decimal_places=2 , default=0)
    image = models.ImageField(upload_to='photos/%Y/%m/%d', default='photos/2025/01/19/flying_cat.jpg')
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']