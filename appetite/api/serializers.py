from rest_framework import serializers
from appetite.api.models import MenuItem, Order, Venue, Category, OrderItem
import pytz

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['url', 'name', 'price', 'extra_info', 'category', 'venue']
        depth = 1


class OrderSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='iso-8601', default_timezone=pytz.utc, read_only=True)

    class Meta:
        model = Order
        fields = ['url', 'status', 'table', 'items', 'created_at']
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
