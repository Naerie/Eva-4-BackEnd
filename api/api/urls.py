from django.contrib import admin
from django.urls import path, include
from main.views import (
    PropiedadList, PropiedadDetail,
    TipoPropiedadList, TipoPropiedadDetail,
    EstadoPropiedadList, EstadoPropiedadDetail,
    OperacionPropiedadList, OperacionPropiedadDetail,
    ComunaList, ComunaDetail,
    ClienteList, ClienteDetail,
    ContactoList, ContactoDetail,
    SuscripcionList, SuscripcionDetail,
    InteresList, InteresDetail
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

urlpatterns = [
    # ADMIN
    path('admin/', admin.site.urls),
    
    # ============================================
    # DOCUMENTACIÓN API (SWAGGER/OPENAPI)
    # ============================================
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    
    # ============================================
    # AUTENTICACIÓN (JWT)
    # ============================================
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # ============================================
    # PROPIEDADES (slug)
    # ============================================
    path('api/propiedades/', PropiedadList.as_view(), name='propiedad-list'),
    path('api/propiedades/<slug:slug>/', PropiedadDetail.as_view(), name='propiedad-detail'),

    # ============================================
    # TIPOS DE PROPIEDAD
    # ============================================
    path('api/tipos-propiedad/', TipoPropiedadList.as_view(), name='tipo-propiedad-list'),
    path('api/tipos-propiedad/<int:pk>/', TipoPropiedadDetail.as_view(), name='tipo-propiedad-detail'),

    # ============================================
    # ESTADOS
    # ============================================
    path('api/estados/', EstadoPropiedadList.as_view(), name='estado-list'),
    path('api/estados/<int:pk>/', EstadoPropiedadDetail.as_view(), name='estado-detail'),

    # ============================================
    # OPERACIONES
    # ============================================
    path('api/operaciones/', OperacionPropiedadList.as_view(), name='operacion-list'),
    path('api/operaciones/<int:pk>/', OperacionPropiedadDetail.as_view(), name='operacion-detail'),

    # ============================================
    # COMUNAS
    # ============================================
    path('api/comunas/', ComunaList.as_view(), name='comuna-list'),
    path('api/comunas/<int:pk>/', ComunaDetail.as_view(), name='comuna-detail'),

    # ============================================
    # CONTACTO
    # ============================================
    path('api/contactos/', ContactoList.as_view(), name='contacto-list'),
    path('api/contactos/<int:pk>/', ContactoDetail.as_view(), name='contacto-detail'),

    # ============================================
    # CLIENTES
    # ============================================
    path('api/clientes/', ClienteList.as_view(), name='cliente-list'),
    path('api/clientes/<int:pk>/', ClienteDetail.as_view(), name='cliente-detail'),

    # ============================================
    # SUSCRIPCIONES
    # ============================================
    path('api/suscripciones/', SuscripcionList.as_view(), name='suscripcion-list'),
    path('api/suscripciones/<int:pk>/', SuscripcionDetail.as_view(), name='suscripcion-detail'),

    # ============================================
    # INTERESES
    # ============================================
    path('api/intereses/', InteresList.as_view(), name='interes-list'),
    path('api/intereses/<int:pk>/', InteresDetail.as_view(), name='interes-detail'),
]