from django.urls import path
from .views import createGateway

path('api/gateways/', createGateway, name='createGateway'),
path('api/routes/', createRoute, name='createRoute'),
path('api/getroute/', getRoute, name='getRoute'),
