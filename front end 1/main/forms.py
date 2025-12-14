from django import forms
import re
from main.models import Contacto, Cliente, Suscripcion


class FormContacto(forms.ModelForm):
    class Meta:
        model = Contacto
        exclude = ['fecha']
        labels = {
            'nombre': 'Nombre:',
            'email': 'Correo electrónico:',
            'nTelefono': 'Número de teléfono:',
            'mensaje': 'Mensaje:'
        }

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingresa tu nombre'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'ejemplo@gmail.com'
            }),
            'nTelefono': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: +56912345678'
            }),
            'mensaje': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Escribe tu mensaje aquí...',
                'rows': 4
            }),
        }

        #validaciones
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if nombre:
            patron = r'^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+$'  
            if not re.fullmatch(patron, nombre):
                raise forms.ValidationError("El nombre solo puede contener letras y espacios.")
        return nombre

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            pat = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if not re.fullmatch(pat, email):
                raise forms.ValidationError("Dirección de correo inválida.")
        return email
            
    def clean_nTelefono(self):
        telefono = self.cleaned_data.get('nTelefono')
        if telefono:
            pat = r'^\+\d{1,3}\d{10}$'
            if not re.fullmatch(pat, telefono):
                raise forms.ValidationError('Numero de telefono inválido.')
        return telefono


class FormCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        exclude = ['fechaCliente']
        labels= {
            'nombreCliente': 'Nombre:',
            'emailCliente': 'Correo electronico:',
            'nTelefonoCliente': 'Número de telefono'
        }
        widgets = {
            'nombreCliente': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingresa tu nombre'
            }),
            'emailCliente': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Correo@gmail.com'
            }),
            'nTelefonoCliente': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+56 9 12345678'
            })
        }
    def clean_nombreCliente(self):
        nombre = self.cleaned_data.get('nombreCliente')
        if nombre:
            patron = r'^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+$'  
            if not re.fullmatch(patron, nombre):
                raise forms.ValidationError("El nombre solo puede contener letras y espacios.")
        return nombre
    
    def clean_emailCliente(self):
        email = self.cleaned_data.get('emailCliente')
        if email:
            pat = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if not re.fullmatch(pat, email):
                raise forms.ValidationError("Dirección de correo inválida.")
        return email
            
    def clean_nTelefonoCliente(self):
        telefono = self.cleaned_data.get('nTelefonoCliente')
        if telefono:
            pat = r'^\+\d{1,3}\d{10}$'
            if not re.fullmatch(pat, telefono):
                raise forms.ValidationError('Numero de telefono inválido.')
        return telefono

class FormSuscripcion(forms.ModelForm):
    class Meta:
        model = Suscripcion
        fields = ['emailSus']
        labels = {
            'emailSus' : ''
        }

        widgets = {
            'emailSus': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tu correo electrónico'
            })
        }
    def clean_emailSus(self):
        email = self.cleaned_data.get('emailSus')
        if email:
            patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if not re.fullmatch(patron, email):
                raise forms.ValidationError("Dirección de correo inválida.")
        if Suscripcion.objects.filter(emailSus=email).exists():
            raise forms.ValidationError("Ya estás suscrito.")
        return email
        
    