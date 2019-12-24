from django.test import TestCase, Client
from django.urls import reverse

from .models import Sensor, Temperatura, Humedad, Planta, Luz

import datetime

from rest_framework.test import APIClient
from rest_framework import status

# Models test
class models_test(TestCase):
    """  Test Module to Create Models and Classmethods """

    def setUp(self):
        self.temp = Temperatura.objects.create(valor=3.12)
        self.hum = Humedad.objects.create(valor=1.12)
        self.planta = Planta.objects.create(valor=4.12)
        self.luz = Luz.objects.create(valor=0.12)

    def test_temperatura(self):
        self.assertEqual(len(list(Temperatura.objects.all())), 1)
        self.assertEqual(float(Temperatura.objects.first().valor), 3.12)

    def test_humedad(self):
        self.assertEqual(len(list(Humedad.objects.all())), 1)
        self.assertEqual(float(Humedad.objects.first().valor), 1.12)

    def test_planta(self):
        self.assertEqual(len(list(Planta.objects.all())), 1)
        self.assertEqual(float(Planta.objects.first().valor), 4.12)

    def test_luz(self):
        self.assertEqual(len(list(Luz.objects.all())), 1)
        self.assertEqual(float(Luz.objects.first().valor), 0.12)

    def test_media(self):
        self.assertEqual(Temperatura.media(), 3.12)
        Temperatura.objects.create(valor=6.24)
        self.assertEqual(Temperatura.media(), 4.68)
        self.assertEqual(Luz.media(), 0.12)

    def test_max(self):
        self.assertEqual(Temperatura.max(), 3.12)
        Temperatura.objects.create(valor=6.24)
        self.assertEqual(Temperatura.max(), 6.24)
        self.assertEqual(Planta.max(), 4.12)

    def test_min(self):
        self.assertEqual(Temperatura.min(), 3.12)
        Temperatura.objects.create(valor=3.12)
        self.assertEqual(Temperatura.min(), 3.12)
        self.assertEqual(Planta.min(), 4.12)

    def test_values_range(self):
        self.assertEqual(len(list(Temperatura.values_dates("2019-12-1", "2025-12-1"))),1)
        Temperatura.objects.create(valor=3.12)
        self.assertEqual(len(list(Temperatura.values_dates("2019-12-1", "2025-12-1"))),2)
        self.assertEqual(len(list(Temperatura.values_dates("2024-12-1", "2025-12-1"))),0)

class views_test(TestCase):
    """  Test Module to Views """

    def setUp(self):
        self.client = APIClient()
        self.temp = Temperatura.objects.create(valor=3.12)
        self.hum = Humedad.objects.create(valor=1.12)
        self.planta = Planta.objects.create(valor=4.12)
        self.luz = Luz.objects.create(valor=0.12)

    def test_temp_view(self):
        response = self.client.get(reverse('temp'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_hum_view(self):
        response = self.client.get(reverse('hum'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_plant_view(self):
        response = self.client.get(reverse('plant'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_luz_view(self):
        response = self.client.get(reverse('luz'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_temp_view_post(self):
        response = self.client.post('/api/temp/', {"valor": 15.6}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_hum_view_post(self):
        response = self.client.post('/api/hum/', {"valor": 25.6}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_plant_view_post(self):
        response = self.client.post('/api/plant/', {"valor": 35.6}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_luz_view_post(self):
        response = self.client.post('/api/luz/', {"valor": 45.6}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)