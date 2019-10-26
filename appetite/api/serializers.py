from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django.core.serializers.json import DjangoJSONEncoder
from appetite.api.models import MenuItem, Order, Venue, Category, OrderItem


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['url', 'name', 'price', 'extra_info', 'category', 'venue']
        depth = 1

class OrderSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField()
    class Meta:
        model = Order
        fields = ['url', 'status', 'customer', 'table', 'items']
        depth = 1


class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = ['url', 'name', 'info']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['url', 'name']


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['url', 'amount', 'item', 'order']
        depth = 2
