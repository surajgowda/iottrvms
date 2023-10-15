from rest_framework import serializers
from .models import VehicleLocation

class VehicleLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleLocation
        fields = '__all__'
