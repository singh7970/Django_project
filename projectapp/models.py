from django.db import models

# Create your models here.
class Basicform(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    
    def __str__(self):
        return self.name
    
class DATA(models.Model):
    name =models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=128) 
    address = models.TextField()
    def __str__(self):
        return self.name
    

class Insta(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    def __str__(self):
        return self.name





  
