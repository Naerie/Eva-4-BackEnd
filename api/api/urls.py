"""
URL configuration for api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from main.views import PropiedadList, PropiedadDetail, TipoPropiedadDetail, TipoPropiedadList, EstadoPropiedadDetail, EstadoPropiedadList, OperacionPropiedadList, OperacionPropiedadDetail, ClienteList,ClienteDetail,ComunaDetail,ComunaList,ContactoDetail,ContactoList,SuscripcionList

urlpatterns = [
    path('api/propiedades/', PropiedadList.as_view()),
    path('api/propiedades/<int:pk>/', PropiedadDetail.as_view()),

    path('api/tipos-propiedad/', TipoPropiedadList.as_view()),
    path('api/tipos-propiedad/<int:pk>/', TipoPropiedadDetail.as_view()),

    path('api/estados/', EstadoPropiedadList.as_view()),
    path('api/estados/<int:pk>/', EstadoPropiedadDetail.as_view()),

    path('api/operaciones/', OperacionPropiedadList.as_view()),
    path('api/operaciones/<int:pk>/', OperacionPropiedadDetail.as_view()),

    path('api/comunas/', ComunaList.as_view()),
    path('api/comunas/<int:pk>/', ComunaDetail.as_view()),

    path('api/contactos/', ContactoList.as_view()),
    path('api/contactos/<int:pk>/', ContactoDetail.as_view()),

    path('api/clientes/', ClienteList.as_view()),
    path('api/clientes/<int:pk>/', ClienteDetail.as_view()),

    path('api/suscripciones/', SuscripcionList.as_view()),
]

