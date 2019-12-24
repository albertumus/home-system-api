from django.contrib import admin
from metricas.models import  Sensor, Temperatura, Humedad, Planta, Luz



admin.site.register(Temperatura)
admin.site.register(Humedad)
admin.site.register(Planta)
admin.site.register(Luz)