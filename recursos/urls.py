from django.urls import path
from . import views

app_name = 'recursos'

urlpatterns = [
    path('', views.index, name='index'),
    # más rutas si las necesitas
]
