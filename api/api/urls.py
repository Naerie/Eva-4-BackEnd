from django.contrib import admin
from django.urls import path
from main.views import (
    PropiedadList, PropiedadDetail,
    TipoPropiedadList, TipoPropiedadDetail,
    EstadoPropiedadList, EstadoPropiedadDetail,
    OperacionPropiedadList, OperacionPropiedadDetail,
    ComunaList, ComunaDetail,
    ClienteList, ClienteDetail,
    ContactoList, ContactoDetail,
    SuscripcionList
)

urlpatterns = [
    # PROPIEDADES (slug)
    path('api/propiedades/', PropiedadList.as_view()),
    path('api/propiedades/<slug:slug>/', PropiedadDetail.as_view()),

    # TIPOS DE PROPIEDAD
    path('api/tipos-propiedad/', TipoPropiedadList.as_view()),
    path('api/tipos-propiedad/<int:pk>/', TipoPropiedadDetail.as_view()),

    # ESTADOS
    path('api/estados/', EstadoPropiedadList.as_view()),
    path('api/estados/<int:pk>/', EstadoPropiedadDetail.as_view()),

    # OPERACIONES
    path('api/operaciones/', OperacionPropiedadList.as_view()),
    path('api/operaciones/<int:pk>/', OperacionPropiedadDetail.as_view()),

    # COMUNAS
    path('api/comunas/', ComunaList.as_view()),
    path('api/comunas/<int:pk>/', ComunaDetail.as_view()),

    # CONTACTO
    path('api/contactos/', ContactoList.as_view()),
    path('api/contactos/<int:pk>/', ContactoDetail.as_view()),

    # CLIENTES
    path('api/clientes/', ClienteList.as_view()),
    path('api/clientes/<int:pk>/', ClienteDetail.as_view()),

    # SUSCRIPCIONES
    path('api/suscripciones/', SuscripcionList.as_view()),
]
