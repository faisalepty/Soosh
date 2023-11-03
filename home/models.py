from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Subcategory(models.Model):
    maincategory = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand_subcat = models.CharField(max_length=50, null=True, blank=True)
    main_subcat = models.CharField(max_length=50, null=True, blank=True)
    def __str__(self):
        if self.brand_subcat:
            return self.brand_subcat
        else:
            return self.main_subcat
        
class Variation(models.Model):
    color = models.CharField(max_length=50, null=True, blank=True)
    size = models.CharField(max_length=50, null=True, blank=True)
    GENDER_CHOICE = (
        ('M', 'MALE'),
        ('F', 'FEMALE'),
        ('U', 'UNISEX')
    )
    gender = models.CharField(choices=GENDER_CHOICE, max_length=50, null=True, blank=True)

    def __str__(self):
        if self.color:
            return self.color
        else:
            return self.size


class Product(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    variation = models.ForeignKey(Variation, on_delete=models.CASCADE, null=True, blank=True)
    subcategory = models.ManyToManyField(Subcategory, null=True, blank=True)
    price = models.FloatField()
    pic = models.ImageField(upload_to=('images'))
   
    def __str__(self):
        return self.name
    


