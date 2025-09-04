from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=120,blank=True, null=True)
    description = models.CharField(max_length=300,blank=True,null=True)
    quantity = models.IntegerField()
    category = models.CharField(max_length=50,blank=True,null=True)
    
    def __str__(self):
        return self.name + " " + self.category
    
    
class Purchase(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.product.name + " " + self.quantity
    
class Suplier(models.Model):
    name = models.CharField(max_length=120,blank=True,null=True)
    email = models.EmailField(max_length=254,blank=True,null=True)
    phone = models.CharField(max_length=120,blank=True,null=True)
    address = models.CharField(max_length=254,blank=True,null=True)
    
    def __str__(self):
        return self.name
    
