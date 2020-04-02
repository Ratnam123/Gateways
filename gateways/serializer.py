from rest_framework import serializers
from .models import Gateway, Route

class gatewaySerializer(serializers.Serializer):
    class Meta:
        model = Gateway
        fields = ['name', 'ip_address']


class routeSerializer(serializers.Serializer):
    class Meta:
	model = Route
	fields = ['prefix', 'gateway_id']

