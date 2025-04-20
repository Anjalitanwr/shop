from django.db import models
from django.conf import settings

from django.contrib.auth.models import User

User=settings.AUTH_USER_MODEL


class Vendor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Product(models.Model):
    ELECTRONICS = 'Electrornics'
    GROCERY = 'Grocery'
    FRUIT = 'Fruite'
    FLOWER = 'Flowers'
    SMARTPHONE = 'Smartphone'
    CLOTH = 'Cloth'
    ANIMAL = 'Animal'
    CATEGORY_CHOICES = [
        (ELECTRONICS, 'Electronics'),
        (GROCERY, 'Grocery'),
        (FRUIT, 'Fruite'),
        (FLOWER, 'Flowers'),
        (SMARTPHONE,'Smart Phone'),
        (CLOTH,'Cloth'),
        (ANIMAL,'Animal'),
    ]
    vender=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField()
    image = models.ImageField(upload_to='product_img', blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default=ELECTRONICS,null=False, blank=True)
    def __str__(self):
        return F"{self.name},{self.category}"




class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="reviews")
    rating = models.PositiveIntegerField(default=0) 
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Review for {self.product.name} by {self.user.username}'