from django.db import models
from datetime import datetime
from django.utils import timezone


class Venue(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.TextField()
    info = models.TextField()


class Category(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.TextField()


class MenuItem(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.TextField()
    price = models.FloatField()
    extra_info = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    venue = models.ForeignKey('Venue', on_delete=models.CASCADE, related_name='menu_items')
    reccomended = models.BooleanField(default=False)


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.TextField()  # staging? > pending > delivered? > payed
    table = models.IntegerField()


class OrderItem(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    amount = models.IntegerField()
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='items')
    item = models.ForeignKey('MenuItem', on_delete=models.DO_NOTHING)

