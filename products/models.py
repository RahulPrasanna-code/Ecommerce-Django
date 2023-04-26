from cProfile import label
from itertools import product
from sre_parse import CATEGORIES
from django.db import models
from django.contrib.auth.models import User

CATEGORY_CHOICES = (
    ('DF','Dairy Farming'),
    ('DP','Dairy Products'),
    ('Fb','Fibres'),
    ('M','Meat'),
    ('NS','Not Specifed')   
)

LABEL_CHOICES = (
    ('best-seller','primary'),
    ('trusted','secondary'),
    ('NEW','danger'),
)

class Seller(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    rating = models.FloatField(default=0.0)
    address = models.TextField()

class Buyer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    contact =  models.CharField(max_length=20)

class Address(models.Model):
    buyer = models.ForeignKey(Buyer,on_delete=models.CASCADE)
    address = models.TextField()

class Product(models.Model):
    name = models.CharField(max_length=255)
    image_url = models.CharField(max_length=10000,default="https://www.cisin.com/coffee-break/components/com_easyblog/themes/wireframe/images/placeholder-image.png")
    description = models.TextField()
    price = models.FloatField()
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    label = models.CharField(choices=LABEL_CHOICES,max_length=20)
    seller = models.ManyToManyField(Seller)
    available_quantity = models.IntegerField()
    rating = models.FloatField(default=0.0)

class OrderProduct(models.Model): #Cart
    buyer = models.ForeignKey(Buyer,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def get_product_total(self):
        return self.product.price*self.quantity

class Order(models.Model):
    buyer = models.ForeignKey(Buyer,on_delete=models.CASCADE)
    date = models.DateTimeField()
    status = models.CharField(max_length=100)




