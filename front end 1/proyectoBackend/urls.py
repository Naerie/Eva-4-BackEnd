"""
URL configuration for proyectoBackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from manager import views as mViews
from main import views as mainViews

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # cliente
    path('', mainViews.index, name="home"),
    path('nosotros/', mainViews.sobreNosotros, name="about"),
    path('contacto/',mainViews.contacto, name="contacto"),
    path('propiedades/<slug:slug>/', mainViews.propiedad, name='detalle-propiedad'),
    path('contacto-success/', mainViews.contactoSuccess, name='c-success'),

    # admin
    path('login/', mViews.logIn, name="login-admin"),
    path('manage/',mViews.homeManager, name='home-manager'),
    path('registroPropiedades/', mViews.registro, name="registro-propiedades"),
    path('propiedades/', mViews.verPropiedades, name="listado-propiedades"),
    path('propiedades/actualizar/<int:id>/', mViews.actualizarPropiedades, name='actualizar-propiedad'),
    path('propiedades/eliminar/<int:id>/', mViews.eliminarPropiedad, name='eliminar-propiedad'),
    path('mensajes/', mViews.verMensajes, name='ver-contacto'),
    path('mensajes/eliminar/<int:id>/', mViews.eliminarMensaje, name='eliminar-contacto'),
    path('gestion/', mViews.gestionar, name='gestion'),
    path('gestion/eliminar/<str:campo>/<int:id>/', mViews.eliminarGestion, name='eliminar-gestion'),
    path('gestion/actualizar/<str:campo>/<int:id>/', mViews.actualizarGestion, name='actualizar-gestion'),
    path('logout/', mViews.cerrar_sesion, name='logout'),
    path('interes/', mViews.Intereses, name='tabla-interes'),
    path('interes/eliminar/<int:id>/', mViews.eliminarInteres, name='eliminar-interes'),
    path('suscripciones/', mViews.verSuscripciones, name='ver-suscripciones')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)