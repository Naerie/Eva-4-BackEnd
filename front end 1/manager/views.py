from django.shortcuts import render, get_object_or_404
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from manager import forms
#from main.models import Contacto, Cliente, Suscripcion, Interes
#from manager.models import Propiedad, TiposPropiedades, Comunas, EstadosPropiedades, OperacionesPropiedades
import requests
from django.conf import settings



def registro(request):
    form = forms.FormRegistrarP()

    if request.method == 'POST':
        form = forms.FormRegistrarP(request.POST, request.FILES)
        if form.is_valid():
            requests.post(
                f"{settings.API_BASE_URL}/propiedades/",
                data=form.cleaned_data,
                files=request.FILES
            )
            return redirect('listado-propiedades')

    return render(request, 'templatesManager/registrarPropiedades.html', {'form': form})


def verPropiedades(request):
    propiedades = requests.get(
        f"{settings.API_BASE_URL}/propiedades/"
    ).json()

    return render(request, 'templatesManager/propiedades.html', {
        'propiedades': propiedades
    })


def eliminarPropiedad(request, id):
    requests.delete(
        f"{settings.API_BASE_URL}/propiedades/{id}/"
    )
    return redirect('listado-propiedades')


def actualizarPropiedades(request, id):
    if request.method == 'POST':
        form = forms.FormRegistrarP(request.POST, request.FILES)
        if form.is_valid():
            requests.put(
                f"{settings.API_BASE_URL}/propiedades/{id}/",
                data=form.cleaned_data,
                files=request.FILES
            )
            return redirect('listado-propiedades')

    return redirect('listado-propiedades')




def logIn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        response = requests.post(
            f"{settings.API_BASE_URL}/token/",
            json={
                "username": username,
                "password": password
            }
        )

        if response.status_code == 200:
            token = response.json()['access']
            request.session['token'] = token
            return redirect('home-manager')

        messages.error(request, 'Usuario o contraseña incorrectos')

    return render(request, 'templatesManager/login.html')




def homeManager(request):
    return render(request, 'templatesManager/manage.html')


def verMensajes(request):
    contacto = requests.get(
        f"{settings.API_BASE_URL}/contactos/"
    ).json()

    return render(request, 'templatesManager/contacto-admin.html', {
        'contacto': contacto
    })


def eliminarMensaje(request, id):
    requests.delete(
        f"{settings.API_BASE_URL}/contactos/{id}/"
    )
    return redirect('ver-contacto')  

def gestionar(request):

    formTipos = forms.FormTiposPropiedades()
    formEstados = forms.FormEstadosPropiedades()
    formOpe = forms.FormOperacionesPropiedades()
    formComuna = forms.FormComunas()

    if request.method == 'POST':
        form_name = request.POST.get('form_name')

        if form_name == 'tipos':
            formTipos = forms.FormTiposPropiedades(request.POST)
            if formTipos.is_valid():
                requests.post(
                    f"{settings.API_BASE_URL}/tipos-propiedad/",
                    json=formTipos.cleaned_data
                )
                return redirect('gestion')

        elif form_name == 'estados':
            formEstados = forms.FormEstadosPropiedades(request.POST)
            if formEstados.is_valid():
                requests.post(
                    f"{settings.API_BASE_URL}/estados/",
                    json=formEstados.cleaned_data
                )
                return redirect('gestion')

        elif form_name == 'operaciones':
            formOpe = forms.FormOperacionesPropiedades(request.POST)
            if formOpe.is_valid():
                requests.post(
                    f"{settings.API_BASE_URL}/operaciones/",
                    json=formOpe.cleaned_data
                )
                return redirect('gestion')

        elif form_name == 'comunas':
            formComuna = forms.FormComunas(request.POST)
            if formComuna.is_valid():
                requests.post(
                    f"{settings.API_BASE_URL}/comunas/",
                    json=formComuna.cleaned_data
                )
                return redirect('gestion')

    # 🔥 LISTAR DESDE API (NO ORM)
    tipos = requests.get(f"{settings.API_BASE_URL}/tipos-propiedad/").json()
    operaciones = requests.get(f"{settings.API_BASE_URL}/operaciones/").json()
    comunas = requests.get(f"{settings.API_BASE_URL}/comunas/").json()
    estados = requests.get(f"{settings.API_BASE_URL}/estados/").json()

    return render(request, 'templatesManager/gestionar.html', {
        'formT': formTipos,
        'formE': formEstados,
        'formO': formOpe,
        'formC': formComuna,
        'tipos': tipos,
        'operaciones': operaciones,
        'comunas': comunas,
        'estados': estados,
    })


def eliminarGestion(request, id, campo):
    endpoint = {
        'tipo': 'tipos-propiedad',
        'estado': 'estados',
        'operacion': 'operaciones',
        'comuna': 'comunas'
    }.get(campo)

    if endpoint:
        requests.delete(
            f"{settings.API_BASE_URL}/{endpoint}/{id}/"
        )

    return redirect('gestion')

    
def actualizarGestion(request, campo, id):

    endpoint = {
        'tipo': 'tipos-propiedad',
        'estado': 'estados',
        'operacion': 'operaciones',
        'comuna': 'comunas'
    }.get(campo)

    if request.method == 'POST' and endpoint:
        requests.put(
            f"{settings.API_BASE_URL}/{endpoint}/{id}/",
            json=request.POST.dict()
        )

    return redirect('gestion')


def cerrar_sesion(request):
    logout(request)
    return redirect('login-admin')

def Intereses(request):
    intereses = requests.get(
        f"{settings.API_BASE_URL}/intereses/"
    ).json()

    return render(request, 'templatesManager/interes.html', {
        'intereses': intereses
    })


def eliminarInteres(request, id):
    requests.delete(
        f"{settings.API_BASE_URL}/intereses/{id}/"
    )
    return redirect('tabla-interes')


def verSuscripciones(request):
    suscripciones = requests.get(
        f"{settings.API_BASE_URL}/suscripciones/"
    ).json()

    return render(request, 'templatesManager/suscripciones.html', {
        'suscripciones': suscripciones
    })
