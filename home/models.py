from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    pic = models.ImageField(upload_to=('images'))
    size = models.IntegerField(null=True)
    BRANDS = (
        ('Nike', 'Nike'),
        ('Jordan', 'Jordan'),
        ('Adidas', 'Adidas'),
    )
    brand = models.CharField(max_length=20, choices=BRANDS, null=True)
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('U', 'Unisex'),
    )
    gender = models.CharField(choices=GENDER, max_length=10, null=True)



    def __str__(self):
        return self.name