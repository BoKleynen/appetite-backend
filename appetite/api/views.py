from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from appetite.api.models import MenuItem, OrderItem, Order, Category, Venue
from appetite.api.serializers import MenuItemSerializer, OrderSerializer, OrderItemSerializer, VenueSerializer, CategorySerializer

from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

@api_view()
def hello_world(request):
    return Response("hello world")



class MenuItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows MenuItems to be viewed or edited.
    """
    queryset = MenuItem.objects.all().order_by('-reccomended')
    serializer_class = MenuItemSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'category', 'venue', 'reccomended']
    depth=1


class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Orders to be viewed or edited.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['table', 'status']


class VenueViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Venues to be viewed or edited.
    """
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Categorys to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows OrderItems to be viewed or edited.
    """
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['item', 'order']
# class
