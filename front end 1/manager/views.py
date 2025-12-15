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
from django.contrib.auth.decorators import login_required
from manager.utils import auth_headers



@login_required(login_url='login-admin')
def registro(request):

    # cargar catálogos
    comunas = requests.get(
        f"{settings.API_BASE_URL}/comunas/",
        headers=auth_headers(request)
    ).json()

    tipos = requests.get(
        f"{settings.API_BASE_URL}/tipos-propiedad/",
        headers=auth_headers(request)
    ).json()

    operaciones = requests.get(
        f"{settings.API_BASE_URL}/operaciones/",
        headers=auth_headers(request)
    ).json()

    estados = requests.get(
        f"{settings.API_BASE_URL}/estados/",
        headers=auth_headers(request)
    ).json()

    form = forms.FormRegistrarP()

    # 🔥 ASIGNAR CHOICES CON ID
    form.fields['comuna'].choices = [
        (c['id'], c['comuna']) for c in comunas
    ]

    form.fields['tipo_propiedad'].choices = [
        (t['id'], t['tipoPropiedad']) for t in tipos
    ]

    form.fields['operacion'].choices = [
        (o['id'], o['operacion']) for o in operaciones
    ]

    form.fields['estado'].choices = [
        (e['id'], e['estado']) for e in estados
    ]

    if request.method == 'POST':
        form = forms.FormRegistrarP(request.POST, request.FILES)

        # volver a cargar choices
        form.fields['comuna'].choices = [(c['id'], c['comuna']) for c in comunas]
        form.fields['tipo_propiedad'].choices = [(t['id'], t['tipoPropiedad']) for t in tipos]
        form.fields['operacion'].choices = [(o['id'], o['operacion']) for o in operaciones]
        form.fields['estado'].choices = [(e['id'], e['estado']) for e in estados]

        if form.is_valid():
            requests.post(
                f"{settings.API_BASE_URL}/propiedades/",
                data=form.cleaned_data,
                files=request.FILES,
                headers=auth_headers(request)
            )
            return redirect('listado-propiedades')

    return render(request, 'templatesManager/registrarPropiedades.html', {'form': form})


@login_required(login_url='login-admin')
def verPropiedades(request):
    propiedades = requests.get(
        f"{settings.API_BASE_URL}/propiedades/", headers=auth_headers(request)
    ).json()

    return render(request, 'templatesManager/propiedades.html', {
        'propiedades': propiedades
    })

@login_required(login_url='login-admin')
def eliminarPropiedad(request, id):
    requests.delete(
        f"{settings.API_BASE_URL}/propiedades/{id}/", headers=auth_headers(request)
    )
    return redirect('listado-propiedades')

@login_required(login_url='login-admin')
def actualizarPropiedades(request, id):
    if request.method == 'POST':
        form = forms.FormRegistrarP(request.POST, request.FILES)
        if form.is_valid():
            requests.put(
                f"{settings.API_BASE_URL}/propiedades/{id}/",
                data=form.cleaned_data,
                files=request.FILES, headers=auth_headers(request)
            

            )
            return redirect('listado-propiedades')

    return redirect('listado-propiedades')


from django.contrib.auth import login as django_login
from django.contrib.auth.models import User

def logIn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        response = requests.post(
            f"{settings.API_BASE_URL}/token/",
            json={"username": username, "password": password}
        )

        if response.status_code == 200:
            token = response.json().get('access')
            if token:
                request.session['token'] = token

                # Autenticar usuario Django
                user = authenticate(request, username=username, password=password)
                if user is None:
                    # Si no existe, crearlo temporalmente (solo para sesión local)
                    user = User.objects.create_user(username=username, password=password)
                django_login(request, user)  # Esto activa @login_required
                return redirect('home-manager')

        messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'templatesManager/login.html')




@login_required(login_url='login-admin')
def homeManager(request):
    return render(request, 'templatesManager/manage.html')

@login_required(login_url='login-admin')
def verMensajes(request):
    contacto = requests.get(
        f"{settings.API_BASE_URL}/contactos/",headers=auth_headers(request)
    ).json()

    return render(request, 'templatesManager/contacto-admin.html', {
        'contacto': contacto
    })

@login_required(login_url='login-admin')
def eliminarMensaje(request, id):
    requests.delete(
        f"{settings.API_BASE_URL}/contactos/{id}/",headers=auth_headers(request)
    )
    return redirect('ver-contacto')  

@login_required(login_url='login-admin')
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
                r = requests.post(
                    f"{settings.API_BASE_URL}/tipos-propiedad/",
                    json=formTipos.cleaned_data, headers=auth_headers(request)
                )
                print("STATUS:", r.status_code)
                print("BODY:", r.text)
                return redirect('gestion')

        elif form_name == 'estados':
            formEstados = forms.FormEstadosPropiedades(request.POST)
            if formEstados.is_valid():
                r = requests.post(
                    f"{settings.API_BASE_URL}/estados/",
                    json=formEstados.cleaned_data, headers=auth_headers(request)
                )
                print("STATUS:", r.status_code)
                print("BODY:", r.text)
                return redirect('gestion')

        elif form_name == 'operaciones':
            formOpe = forms.FormOperacionesPropiedades(request.POST)
            if formOpe.is_valid():
                r = requests.post(
                    f"{settings.API_BASE_URL}/operaciones/",
                    json=formOpe.cleaned_data, headers=auth_headers(request)
                )
                print("STATUS:", r.status_code)
                print("BODY:", r.text)
                return redirect('gestion')

        elif form_name == 'comunas':
            formComuna = forms.FormComunas(request.POST)
            if formComuna.is_valid():
                r = requests.post(
                    f"{settings.API_BASE_URL}/comunas/",
                    json=formComuna.cleaned_data ,headers=auth_headers(request)
                )
                print("STATUS:", r.status_code)
                print("BODY:", r.text)
                return redirect('gestion')

    # 🔥 LISTAR DESDE API (NO ORM)
    tipos = requests.get(f"{settings.API_BASE_URL}/tipos-propiedad/",headers=auth_headers(request)).json()
    operaciones = requests.get(f"{settings.API_BASE_URL}/operaciones/",headers=auth_headers(request)).json()
    comunas = requests.get(f"{settings.API_BASE_URL}/comunas/",headers=auth_headers(request)).json()
    estados = requests.get(f"{settings.API_BASE_URL}/estados/",headers=auth_headers(request)).json()

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

@login_required(login_url='login-admin')
def eliminarGestion(request, id, campo):
    endpoint = {
        'tipo': 'tipos-propiedad',
        'estado': 'estados',
        'operacion': 'operaciones',
        'comuna': 'comunas'
    }.get(campo)

    if endpoint:
        requests.delete(
            f"{settings.API_BASE_URL}/{endpoint}/{id}/", headers=auth_headers(request)
        )

    return redirect('gestion')

@login_required(login_url='login-admin')
def actualizarGestion(request, campo, id):

    endpoint = {
        'tipo': 'tipos-propiedad',
        'estado': 'estados',
        'operacion': 'operaciones',
        'comuna': 'comunas'
    }.get(campo)

    if request.method == 'POST' and endpoint:
        data = request.POST.dict()
        data.pop('form_name', None)

        requests.put(
            f"{settings.API_BASE_URL}/{endpoint}/{id}/",
            json=data,
            headers=auth_headers(request)
        )

    return redirect('gestion')


@login_required(login_url='login-admin')
def cerrar_sesion(request):
    logout(request)
    return redirect('login-admin')

@login_required(login_url='login-admin')
def Intereses(request):
    intereses = requests.get(
        f"{settings.API_BASE_URL}/intereses/"
    ).json()

    return render(request, 'templatesManager/interes.html', {
        'intereses': intereses
    })

@login_required(login_url='login-admin')
def eliminarInteres(request, id):
    requests.delete(
        f"{settings.API_BASE_URL}/intereses/{id}/",headers=auth_headers(request)
    )
    return redirect('tabla-interes')

@login_required(login_url='login-admin')
def verSuscripciones(request):
    suscripciones = requests.get(
        f"{settings.API_BASE_URL}/suscripciones/",headers=auth_headers(request)
    ).json()

    return render(request, 'templatesManager/suscripciones.html', {
        'suscripciones': suscripciones
    })

