from django.db import models

class Order(models.Model):
    order_number = models.CharField(max_length=20)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    items = models.ManyToManyField('Item', through='OrderItem')
    date_created = models.DateTimeField(auto_now_add=True)

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=200)

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()

