from django.db import models

# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=100)
    desc=models.CharField(max_length=250)
    price=models.IntegerField()
    img=models.ImageField(upload_to='static/images',blank=True)

