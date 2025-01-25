from django.db import models

# Create your models here.




class Female(models.Model):
    name_female = models.CharField(max_length=100,null=True, blank=True)
    def  __str__(self):
        return self.name_female

class Male(models.Model):
    name_male = models.CharField(max_length=100,null=True, blank=True)
    girls = models.OneToOneField(Female, on_delete=models.PROTECT)

    def  __str__(self):
        return self.name_male
