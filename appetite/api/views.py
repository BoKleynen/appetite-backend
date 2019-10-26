from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from appetite.api.models import MenuItem, OrderItem, Order, Category, Venue
from appetite.api.serializers import UserSerializer, GroupSerializer, MenuItemSerializer, OrderSerializer, OrderItemSerializer, VenueSerializer, CategorySerializer


# Create your views here.

@api_view()
def hello_world(request):
    return Response("hello world")


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class MenuItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows MenuItems to be viewed or edited.
    """
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Orders to be viewed or edited.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


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
# class
