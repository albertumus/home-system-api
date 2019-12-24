from django.urls import path
from django.conf.urls import url

from metricas import views

urlpatterns = [
    url(r'^api/temp/$', views.TemperaturaInformation.as_view() , name="temp"),
    url(r'^api/hum/$', views.HumedadInformation.as_view() , name="hum"),
    url(r'^api/plant/$', views.PlantaInformation.as_view() , name="plant"),
    url(r'^api/luz/$', views.LuzInformation.as_view() , name="luz")
]