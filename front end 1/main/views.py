from django.shortcuts import render ,redirect,get_object_or_404
from django.http import JsonResponse
from main import forms
from manager.models import Propiedad, OperacionesPropiedades, TiposPropiedades, Comunas, EstadosPropiedades
from main.models import Cliente, Interes

#datos.py
from datos import about


# Create your views here.

def index(request):
    propiedades = Propiedad.objects.all().order_by('-fecha')

    # busqueda
    operacion_id = request.GET.get('operacion')
    tipo_id = request.GET.get('tipo')
    comuna_id = request.GET.get('comuna')

    if operacion_id:
        propiedades = propiedades.filter(operacion_id=operacion_id)
    if tipo_id:
        propiedades = propiedades.filter(tipo_propiedad_id=tipo_id)
    if comuna_id:
        propiedades = propiedades.filter(comuna_id=comuna_id)

    # suscripcion
    formulario = forms.FormSuscripcion()
    if request.method == 'POST':
        formulario = forms.FormSuscripcion(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('home')  

    data = {
        'propiedades': propiedades,
        'form': formulario,
        'operacion': OperacionesPropiedades.objects.all(),
        'tipos_propiedades': TiposPropiedades.objects.all(),
        'comuna': Comunas.objects.all(),
    }

    return render(request, 'templatesMain/home.html', data)

def propiedad(request, slug):
    propiedad = get_object_or_404(Propiedad, slug=slug)
    formulario = forms.FormCliente()

    if request.method == 'POST':
        formulario = forms.FormCliente(request.POST)
        if formulario.is_valid():
            email = formulario.cleaned_data['emailCliente']
            nombre = formulario.cleaned_data['nombreCliente']
            telefono = formulario.cleaned_data['nTelefonoCliente']

            cliente, _ = Cliente.objects.get_or_create(
                emailCliente=email,
                defaults={
                    'nombreCliente': nombre,
                    'nTelefonoCliente': telefono
                }
            )

            Interes.objects.get_or_create(
                cliente=cliente,
                propiedad=propiedad
            )

            return redirect('c-success')

    data = {
        'propiedad': propiedad,
        'form': formulario
    }
    return render(request, 'templatesMain/propiedad.html', data)


    data = {
        'propiedad': propiedad,
        'form': formulario
    }
    return render(request, 'templatesMain/propiedad.html', data)

def sobreNosotros(request):
    return render (request, 'templatesMain/nosotros.html', about)


def contacto(request):
    formulario = forms.FormContacto()
    if request.method == 'POST':
        formulario = forms.FormContacto(request.POST)
        if formulario.is_valid():
            print('formulario de contacto valido')
            formulario.save()
            return redirect('c-success')    
    data = {'form' : formulario}
    return render(request, 'templatesMain/contacto.html', data)


def contactoSuccess(request):
    return render(request, 'templatesMain/contacto-success.html')

