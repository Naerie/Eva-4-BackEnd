from django.shortcuts import render ,redirect,get_object_or_404
from django.http import JsonResponse
from main import forms
import requests
#from manager.models import Propiedad, OperacionesPropiedades, TiposPropiedades, Comunas, EstadosPropiedades
#from main.models import Cliente, Interes
from django.conf import settings
#datos.py
from datos import about
# Create your views here.

def index(request):
    # filtros
    params = {}
    if request.GET.get('operacion'):
        params['operacion'] = request.GET.get('operacion')
    if request.GET.get('tipo'):
        params['tipo_propiedad'] = request.GET.get('tipo')
    if request.GET.get('comuna'):
        params['comuna'] = request.GET.get('comuna')

    propiedades = requests.get(
        f"{settings.API_BASE_URL}/propiedades/",
        params=params
    ).json()

    # selects
    operaciones = requests.get(f"{settings.API_BASE_URL}/operaciones/").json()
    tipos = requests.get(f"{settings.API_BASE_URL}/tipos-propiedad/").json()
    comunas = requests.get(f"{settings.API_BASE_URL}/comunas/").json()

    # suscripción
    formulario = forms.FormSuscripcion()
    if request.method == 'POST':
        formulario = forms.FormSuscripcion(request.POST)
        if formulario.is_valid():
            requests.post(
                f"{settings.API_BASE_URL}/suscripciones/",
                json=formulario.cleaned_data
            )
            return redirect('home')

    data = {
        'propiedades': propiedades,
        'form': formulario,
        'operacion': operaciones,
        'tipos_propiedades': tipos,
        'comuna': comunas,
    }

    return render(request, 'templatesMain/home.html', data)


def propiedad(request, slug):
    response = requests.get(
        f"{settings.API_BASE_URL}/propiedades/{slug}/"
    )

    if response.status_code != 200:
        return redirect('home')

    propiedad = response.json()

    formulario = forms.FormCliente()

    if request.method == 'POST':
        formulario = forms.FormCliente(request.POST)
        if formulario.is_valid():
            requests.post(
                f"{settings.API_BASE_URL}/clientes/",
                json=formulario.cleaned_data
            )
            return redirect('c-success')

    return render(request, 'templatesMain/propiedad.html', {
        'propiedad': propiedad,
        'form': formulario
    })





def sobreNosotros(request):
    return render (request, 'templatesMain/nosotros.html', about)


def contacto(request):
    formulario = forms.FormContacto()

    if request.method == 'POST':
        formulario = forms.FormContacto(request.POST)
        if formulario.is_valid():
            requests.post(
                f"{settings.API_BASE_URL}/contactos/",
                json=formulario.cleaned_data
            )
            return redirect('c-success')

    return render(request, 'templatesMain/contacto.html', {
        'form': formulario
    })



def contactoSuccess(request):
    return render(request, 'templatesMain/contacto-success.html')

