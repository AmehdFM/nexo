# teoria/urls.py
from django.urls import path
from . import views

app_name = 'teoria'  # ✅ Esto es esencial para que funcione el namespace

urlpatterns = [
    path('', views.index, name='index'),
    # otras rutas...
]
