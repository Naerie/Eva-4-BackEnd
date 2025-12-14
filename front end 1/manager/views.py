from django.shortcuts import render, get_object_or_404
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from manager import forms
from main.models import Contacto, Cliente, Suscripcion, Interes
from manager.models import Propiedad, TiposPropiedades, Comunas, EstadosPropiedades, OperacionesPropiedades

@login_required(login_url='login-admin')
@user_passes_test(lambda u: u.is_staff or u.is_superuser, login_url='login-admin')
def registro(request):
    formulario = forms.FormRegistrarP()
    if request.method == 'POST':
        formulario = forms.FormRegistrarP(request.POST, request.FILES)
        if formulario.is_valid():
            print('formulario de registro de propiedades valido')
            formulario.save()
            return redirect('listado-propiedades')
    data = {'form' : formulario}
    return render(request, 'templatesManager/registrarPropiedades.html', data)

@login_required(login_url='login-admin')
@user_passes_test(lambda u: u.is_staff or u.is_superuser, login_url='login-admin')
def verPropiedades(request):
    propiedades = []
    for prop in Propiedad.objects.all():
        propiedades.append({
            'obj': prop,
            'form': forms.FormRegistrarP(instance=prop)  # formulario precargado
        })

    return render(request, 'templatesManager/propiedades.html', {
        'propiedades': propiedades
    })

@login_required(login_url='login-admin')
@user_passes_test(lambda u: u.is_staff or u.is_superuser, login_url='login-admin')
def eliminarPropiedad(request, id):
    propiedad = get_object_or_404(Propiedad, id=id)
    propiedad.delete()  
    return redirect('listado-propiedades')  

@login_required(login_url='login-admin')
@user_passes_test(lambda u: u.is_staff or u.is_superuser, login_url='login-admin')
def actualizarPropiedades(request, id):
    # ACTUALIZAR
    propiedad = get_object_or_404(Propiedad, id=id)
    if request.method == 'POST':
        form = forms.FormRegistrarP(request.POST, request.FILES, instance=propiedad)
        if form.is_valid():
            form.save()
            return redirect('listado-propiedades') 
    else:
        form = forms.FormRegistrarP(instance=propiedad)

    data = {'form' : form,
            'propiedad':propiedad}
    return render(request, 'templatesManager/propiedades.html', data)


def logIn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and (user.is_staff or user.is_superuser):
            login(request, user)
            return redirect('home-manager')  
        else:
            messages.error(request, 'Credenciales inválidas o sin permisos.')
    return render(request, 'templatesManager/login.html')


@login_required(login_url='login-admin')
@user_passes_test(lambda u: u.is_staff or u.is_superuser, login_url='login-admin')
def homeManager(request):
    return render(request, 'templatesManager/manage.html')

@login_required(login_url='login-admin')
@user_passes_test(lambda u: u.is_staff or u.is_superuser, login_url='login-admin')
def verMensajes(request):
    contacto = Contacto.objects.all()
    return render(request, 'templatesManager/contacto-admin.html', {'contacto':contacto})

@login_required(login_url='login-admin')
@user_passes_test(lambda u: u.is_staff or u.is_superuser, login_url='login-admin')
def eliminarMensaje(request, id):
    propiedad = get_object_or_404(Contacto, id=id)
    propiedad.delete()  
    return redirect('ver-contacto')  

@login_required(login_url='login-admin')
@user_passes_test(lambda u: u.is_staff or u.is_superuser, login_url='login-admin')
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
                formTipos.save()
                return redirect('gestion')

        elif form_name == 'estados':
            formEstados = forms.FormEstadosPropiedades(request.POST)
            if formEstados.is_valid():
                formEstados.save()
                return redirect('gestion')

        elif form_name == 'operaciones':
            formOpe = forms.FormOperacionesPropiedades(request.POST)
            if formOpe.is_valid():
                formOpe.save()
                return redirect('gestion')

        elif form_name == 'comunas':
            formComuna = forms.FormComunas(request.POST)
            if formComuna.is_valid():
                formComuna.save()
                return redirect('gestion')

    # recuperar los registros
    tipos = TiposPropiedades.objects.all()
    operaciones = OperacionesPropiedades.objects.all()
    comunas = Comunas.objects.all()
    estados = EstadosPropiedades.objects.all()

    data = {
        'formT': formTipos,
        'formE': formEstados,
        'formO': formOpe,
        'formC': formComuna,
        'tipos': tipos,
        'operaciones': operaciones,
        'comunas': comunas,
        'estados': estados,
    }
    return render(request, 'templatesManager/gestionar.html', data)

@login_required(login_url='login-admin')
@user_passes_test(lambda u: u.is_staff or u.is_superuser, login_url='login-admin')
def eliminarGestion(request, id, campo): 
    if campo == 'tipo':
        objeto = get_object_or_404(TiposPropiedades, id=id)
    elif campo == 'estado':
        objeto = get_object_or_404(EstadosPropiedades, id=id)
    elif campo == 'operacion':
        objeto = get_object_or_404(OperacionesPropiedades, id=id)
    elif campo == 'comuna':
        objeto = get_object_or_404(Comunas, id=id)
    else:
        return redirect('gestion')
    
    objeto.delete()
    return redirect('gestion')
    

@login_required(login_url='login-admin')
@user_passes_test(lambda u: u.is_staff or u.is_superuser, login_url='login-admin')
def actualizarGestion(request, campo, id):
    if campo == 'tipo':
        objeto = get_object_or_404(TiposPropiedades, id=id)
        form = forms.FormTiposPropiedades
    elif campo == 'estado':
        objeto = get_object_or_404(EstadosPropiedades, id=id)
        form = forms.FormEstadosPropiedades
    elif campo == 'operacion':
        objeto = get_object_or_404(OperacionesPropiedades, id=id)
        form = forms.FormOperacionesPropiedades
    elif campo == 'comuna':
        objeto = get_object_or_404(Comunas, id=id)
        form = forms.FormComunas
    else:
        return redirect('gestion')

    if request.method == 'POST':
        form = form(request.POST, instance=objeto)
        if form.is_valid():
            form.save()
            return redirect('gestion')
    else:
        form = form(instance=objeto)
        return redirect('gestion')

@login_required(login_url='login-admin')
@user_passes_test(lambda u: u.is_staff or u.is_superuser, login_url='login-admin')
def cerrar_sesion(request):
    logout(request)
    return redirect('login-admin')

@login_required(login_url='login-admin')
@user_passes_test(lambda u: u.is_staff or u.is_superuser, login_url='login-admin')
def Intereses(request):
    intereses = Interes.objects.select_related('cliente', 'propiedad').all()
    return render(request, 'templatesManager/interes.html', {'intereses': intereses})

@login_required(login_url='login-admin')
@user_passes_test(lambda u: u.is_staff or u.is_superuser, login_url='login-admin')
def eliminarInteres(request, id):
    interes = get_object_or_404(Interes, id=id)
    interes.delete()
    return redirect('tabla-interes') 

@login_required(login_url='login-admin')
@user_passes_test(lambda u: u.is_staff or u.is_superuser, login_url='login-admin')
def verSuscripciones(request):
    sus = Suscripcion.objects.all()
    return render(request, 'templatesManager/suscripciones.html', {'suscripciones':sus})