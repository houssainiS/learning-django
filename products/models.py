from django.db import models
from datetime import datetime
# Create your models here.

class Product(models.Model):
    x=[
        ('phone','phone'),('computer','computer')
    ]

    name = models.CharField(max_length=100 ,default='empety' , verbose_name='Title') 
    content = models.TextField(null=True , blank=True) 
    price = models.DecimalField(max_digits=10, decimal_places=2 , default=0)
    image = models.ImageField(upload_to='photos/%Y/%m/%d', default='photos/2025/01/19/flying_cat.jpg')
    active = models.BooleanField(default=True)
    catigory = models.CharField(max_length=50, null=True , blank=True , choices=x) #added the choices in the list x


    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']



class Test(models.Model):
    date = models.DateField()
    time = models.TimeField(null=True , blank=True)
    created = models.DateTimeField(default=datetime.now) #saving current time
    