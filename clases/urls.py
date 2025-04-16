from django.urls import path
from . import views

app_name = 'clases'  # Esto define el namespace para las URLs de esta app

urlpatterns = [
    path('', views.index, name='index'),  # Lista de clases
    path('<slug:slug>/', views.detalle_clase, name='detalle'),  # Detalle de una clase específica
    # Puedes agregar más URLs si lo necesitas, por ejemplo:
    # path('categoria/<str:categoria>/', views.clases_por_categoria, name='por_categoria'),
    # path('nivel/<str:nivel>/', views.clases_por_nivel, name='por_nivel'),
]