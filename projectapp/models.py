from django.db import models

# Create your models here.
class Basicform(models.Model):
    name=models.CharField(max_length=50),
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    address=models.TextField()


    def __str__(self):
        return self.name

