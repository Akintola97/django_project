from django.db import models
from django.contrib.auth.models import User 


class Customer(models.Model):
    
    user = models.OneToOneField(User, null = False, blank = True, on_delete= models.CASCADE)
    name = models.CharField(max_length = 200, null = True)
    email = models.CharField(max_length = 200, null = True)
    
    def str (self):
        return self.name

    
class Product(models.Model):
    name = models.CharField(max_length=200, null = True)
    price =models.FloatField()
    digital = models.BooleanField(default=False, null = True, blank = False)
    

def str (self):
    return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank = True, null = True)
    date_ordered = models.DateTimeField(auto_now_add = True)
    complete = models.BooleanField(default = False, null = True, blank = False)
    transaction_id = models.CharField(max_length = 200, null = True)
    
    def str (self):
        return str(self.id)


class OrderItem(models.Model):
    prodcut = models.ForeignKey(Product, on_delete = models.SET_NULL, blank = True, null = True)
    order = models.ForeignKey (Order, on_delete = models.SET_NULL, blank = True, null =True)
    quantity = models.IntegerField(default = 0, null = True, blank = True)
    date_added = models.DateTimeField(auto_now_add = True)
    

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null = True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null = True)
    address = models.CharField(max_length=200, null = False)
    city = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length = 200, null = False)
    date_added = models.DateTimeField(auto_now_add = True)
    
    def str (self):
        return self.address
    