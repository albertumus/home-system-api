from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from metricas.serializers import TemperatureSerializer, HumedadSerializer, PlantaSerializer, LuzSerializer

from metricas.models import Temperatura, Humedad, Planta, Luz

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

class SensorSwitchMixin:

    def retrieve_last(self, request, instance):
        last = instance.objects.last()
        return {"temp": last.valor, "time": last.fecha}

class TemperaturaInformation(APIView, SensorSwitchMixin):

    def get(self, requests):

        instance = Temperatura
        
        data = self.retrieve_last(self.request, instance)
        return JSONResponse({"temp":data}, status=status.HTTP_200_OK)

    def post(self, requests):

        jsonData = JSONParser().parse(requests)
        serializer = TemperatureSerializer(data=jsonData)
        
        if ( serializer.is_valid() ):
            serializer.save()
            return JSONResponse(serializer.data, status=status.HTTP_200_OK)
    

class HumedadInformation(APIView, SensorSwitchMixin):

    def get(self, requests):

        instance = Humedad
        data = self.retrieve_last(self.request, instance)

        return JSONResponse({"temp":data}, status=status.HTTP_200_OK)

    def post(self, requests):

        jsonData = JSONParser().parse(requests)
        serializer = HumedadSerializer(data=jsonData)
        
        if ( serializer.is_valid() ):
            serializer.save()
            return JSONResponse(serializer.data, status=status.HTTP_200_OK)

class PlantaInformation(APIView, SensorSwitchMixin):

    def get(self, requests):

        instance = Planta
        data = self.retrieve_last(self.request, instance)

        return JSONResponse({"temp":data}, status=status.HTTP_200_OK)

    def post(self, requests):

        jsonData = JSONParser().parse(requests)
        serializer = PlantaSerializer(data=jsonData)
        
        if ( serializer.is_valid() ):
            serializer.save()
            return JSONResponse(serializer.data, status=status.HTTP_200_OK)

class LuzInformation(APIView, SensorSwitchMixin):

    def get(self, requests):

        instance = Luz
        data = self.retrieve_last(self.request, instance)

        return JSONResponse({"temp":data}, status=status.HTTP_200_OK)

    def post(self, requests):

        jsonData = JSONParser().parse(requests)
        serializer = LuzSerializer(data=jsonData)
        
        if ( serializer.is_valid() ):
            serializer.save()
            return JSONResponse(serializer.data, status=status.HTTP_200_OK)




