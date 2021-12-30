from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, null=False)
    price = models.FloatField(default=0)
    digital = models.BooleanField(default=False, null=True, blank=True)
    # available_stock = models.FloatField(default=0)
    # image = models.ImageField()

    def __str__(self):
        return self.name


class Order(models.Model):
    name = models.CharField(max_length=100)
    date_order = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    transaction_id = models.CharField(max_length=200, null=True)
    # amount_total = models.FloatField(default=0)

    def __str__(self):
        return "{}-{}".format(self.name, str(self.id))


class OrderItem(models.Model):
    name = models.CharField(max_length=100)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.FloatField(default=0)
    # price_subtotal = models.FloatField()
    

class ShippingAddress(models.Model):
    name = models.CharField(max_length=100)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=100, null=True)
    zip_code = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
