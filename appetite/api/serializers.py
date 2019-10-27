from rest_framework import serializers
from appetite.api.models import MenuItem, Order, Venue, Category, OrderItem
import pytz

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['url', 'name', 'price', 'extra_info', 'category', 'venue']
        depth = 1


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['url', 'status', 'table', 'items', 'created_at']
        depth = 1


class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = ['url', 'name', 'info', 'created_at', 'updated_at']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['url', 'name']


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['url', 'amount', 'item', 'order']
        depth = 2
