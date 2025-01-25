from django.db import models

# Create your models here.



# ONE TO ONE RELATIONSHIP
class Female(models.Model):
    name_female = models.CharField(max_length=100,null=True, blank=True)
    def  __str__(self):
        return self.name_female

class Male(models.Model):
    name_male = models.CharField(max_length=100,null=True, blank=True)
    girls = models.OneToOneField(Female, on_delete=models.PROTECT)

    def  __str__(self):
        return self.name_male

#ONE TO MANY RELATIONSHIP

class Product(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    def  __str__(self):
        return self.title


class User(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    def  __str__(self):
        return self.name
    
