from django.shortcuts import render ,redirect,get_object_or_404
from django.http import JsonResponse
from main import forms
import requests
#from manager.models import Propiedad, OperacionesPropiedades, TiposPropiedades, Comunas, EstadosPropiedades
#from main.models import Cliente, Interes

#datos.py
from datos import about

API_BASE = "http://127.0.0.1:8000/api"


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
        f"{API_BASE}/propiedades/",
        params=params
    ).json()

    # selects
    operaciones = requests.get(f"{API_BASE}/operaciones/").json()
    tipos = requests.get(f"{API_BASE}/tipos-propiedad/").json()
    comunas = requests.get(f"{API_BASE}/comunas/").json()

    # suscripción
    formulario = forms.FormSuscripcion()
    if request.method == 'POST':
        formulario = forms.FormSuscripcion(request.POST)
        if formulario.is_valid():
            requests.post(
                f"{API_BASE}/suscripciones/",
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
    propiedades = requests.get(f"{API_BASE}/propiedades/").json()
    propiedad = next((p for p in propiedades if p['slug'] == slug), None)

    if not propiedad:
        return redirect('home')

    formulario = forms.FormCliente()

    if request.method == 'POST':
        formulario = forms.FormCliente(request.POST)
        if formulario.is_valid():
            requests.post(
                f"{API_BASE}/clientes/",
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
                f"{API_BASE}/contactos/",
                json=formulario.cleaned_data
            )
            return redirect('c-success')

    return render(request, 'templatesMain/contacto.html', {
        'form': formulario
    })



def contactoSuccess(request):
    return render(request, 'templatesMain/contacto-success.html')

