from django.contrib.auth.models import User, Group
from rest_framework import serializers
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


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['url', 'status', 'customer', 'table', 'items', 'created_at']


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
