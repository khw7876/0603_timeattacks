from datetime import datetime
from operator import mod
from unicodedata import category
from django.db import models

# Create your models here.
class product(models.Model):
    class Meta:
        db_table = 'product'
    product_title = models.CharField(max_length=128,unique=True)
    product_category = models.CharField(max_length=128,unique=True)
    product_image = models.URLField()
    product_intro = models.TextField()
    product_price = models.IntegerField()
    product_stock = models.IntegerField()

class Category(models.Model):
    class Meta:
        db_table = "category"
    category_name = models.ForeignKey(product, on_delete=models.CASCADE)

class OrderStatus(models.Model):
    class Meta:
        db_table = 'order_Status'

    order_complate = models.BooleanField()
    order_complate = models.BooleanField()
    order_complate = models.BooleanField()
    order_complate = models.BooleanField()

class ProductOrder(models.Model):
    class Meta:
        db_table = "produect_order"
    product_count = models.IntegerField()

class UserOrder(models.Model):
    class Meta:
        db_table = "User_Order"
    user_address = models.TextField()
    order_time = models.DateField()
    all_price = models.IntegerField()
    discount_per = models.IntegerField()
    total_price = models.IntegerField()
    order_valid = models.BooleanField()

