from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=120,blank=True, null=True)
    description = models.CharField(max_length=300,blank=True,null=True)
    quantity = models.IntegerField(max_length=4)
    category = models.CharField(max_length=50,blank=True,null=True)
    
    def __str__(self):
        return self.name + " " + self.category
    
    
