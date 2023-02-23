from rest_framework import serializers
from .models import Shopper

class ShopperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shopper
        fields = '__all__'

