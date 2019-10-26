from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .models import MenuItem, OrderItem, Order, Category, Venue
from .serializers import UserSerializer, GroupSerializer, MenuItemSerializer


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
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = MenuItem.objects
    serializer_class = MenuItemSerializer


# class
