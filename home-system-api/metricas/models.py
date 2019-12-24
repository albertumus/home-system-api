from django.db import models
from django.db.models import Avg, Max, Min

class Sensor(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    valor = models.DecimalField(max_digits=5, decimal_places=2)

    @classmethod
    def media(cls):
        return float(cls.objects.aggregate(Avg('valor'))['valor__avg']) 

    @classmethod
    def max(cls):
        return float(cls.objects.aggregate(Max('valor'))['valor__max'])

    @classmethod
    def min(cls):
        return float(cls.objects.aggregate(Min('valor'))['valor__min'])

    @classmethod
    def values_dates(cls, date1, date2):
        return cls.objects.filter(fecha__range=[date1, date2])

class Temperatura(Sensor):

    def __str__(self):
        return str(self.fecha)
    
    class Meta():
        verbose_name = "temperatura"
        verbose_name_plural = "mediciones temperaturas"

class Humedad(Sensor):

    def __str__(self):
        return str(self.fecha)
    
    class Meta():
        verbose_name = "humedad"
        verbose_name_plural = "mediciones humedad"

class Planta(Sensor):

    def __str__(self):
        return str(self.fecha)
    
    class Meta():
        verbose_name = "planta"
        verbose_name_plural = "mediciones plantas"

class Luz(Sensor):

    def __str__(self):
        return str(self.fecha)
    
    class Meta():
        verbose_name = "luz"
        verbose_name_plural = "mediciones luces"


    



