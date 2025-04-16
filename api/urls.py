"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import teoria.urls
import ejercicios.urls 
import recursos.urls 
import clases.urls 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('teoria/', include('teoria.urls', namespace='teoria')),
    path('ejercicios/', include('ejercicios.urls', namespace='ejercicios')),
    path('recursos/', include('recursos.urls', namespace='recursos')),
    path('clases/', include('clases.urls', namespace='clases'))
]
