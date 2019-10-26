from django.urls import include, path
from appetite.api import views

urlpatterns = [
    # path('users/', include('users.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('hello_world', views.hello_world),
]
