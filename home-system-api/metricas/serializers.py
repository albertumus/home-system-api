from rest_framework import serializers
from metricas.models import Temperatura, Humedad, Planta, Luz

class TemperatureSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Temperatura.objects.create(**validated_data)

    class Meta:
        model = Temperatura
        fields = ['fecha','valor']

class HumedadSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Humedad.objects.create(**validated_data)

    class Meta:
        model = Humedad
        fields = ['fecha','valor']

class PlantaSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Planta.objects.create(**validated_data)

    class Meta:
        model = Planta
        fields = ['fecha','valor']

class LuzSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Luz.objects.create(**validated_data)

    class Meta:
        model = Luz
        fields = ['fecha','valor']

