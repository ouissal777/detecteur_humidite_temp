from rest_framework import serializers
from .models import Dht11


class DHT11serialize(serializers.ModelSerializer):
    temperature = serializers.FloatField(source="temp")
    humidity = serializers.FloatField(source="hum")
    date = serializers.DateTimeField(source="dt", read_only=True)

    class Meta:
        model = Dht11
        fields = ["id", "temperature", "humidity", "date"]
        read_only_fields = ["id", "date"]