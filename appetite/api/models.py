from django.db import models
from django.contrib.auth.models import User


def timestamps(klass):
    klass.created = models.DateTimeField(auto_now_add=True)
    klass.updated = models.DateTimeField(auto_now=True)
    return klass


@timestamps
class Venue(models.Model):
    name = models.TextField()
    info = models.TextField()


@timestamps
class Category(models.Model):
    name = models.TextField()


@timestamps
class MenuItem(models.Model):
    name = models.TextField()
    price = models.FloatField()
    extra_info = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    venue = models.ForeignKey('Venue', on_delete=models.CASCADE, related_name='menu_items')


@timestamps
class Order(models.Model):
    status = models.TextField()  # staging? > pending > delivered? > payed
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.IntegerField()


@timestamps
class OrderItem(models.Model):
    amount = models.IntegerField()
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    item = models.ForeignKey('MenuItem', on_delete=models.DO_NOTHING, related_name='items')

