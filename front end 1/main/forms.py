from django import forms
import re


class FormContacto(forms.Form):
    nombre = forms.CharField(
        max_length=50,
        label='Nombre',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingresa tu nombre'
        })
    )
    email = forms.EmailField(
        label='Correo electrónico',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'ejemplo@gmail.com'
        })
    )
    nTelefono = forms.CharField(
        label='Número de teléfono',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '+56912345678'
        })
    )
    mensaje = forms.CharField(
        label='Mensaje',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Escribe tu mensaje aquí...',
            'rows': 4
        })
    )

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if not re.fullmatch(r'^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+$', nombre):
            raise forms.ValidationError("El nombre solo puede contener letras y espacios.")
        return nombre

    def clean_nTelefono(self):
        telefono = self.cleaned_data['nTelefono']
        if not re.fullmatch(r'^\+\d{11,13}$', telefono):
            raise forms.ValidationError("Número de teléfono inválido.")
        return telefono

class FormCliente(forms.Form):
    nombreCliente = forms.CharField(
        max_length=50,
        label='Nombre',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingresa tu nombre'
        })
    )
    emailCliente = forms.EmailField(
        label='Correo electrónico',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'correo@gmail.com'
        })
    )
    nTelefonoCliente = forms.CharField(
        label='Número de teléfono',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '+56912345678'
        })
    )

    def clean_nombreCliente(self):
        nombre = self.cleaned_data['nombreCliente']
        if not re.fullmatch(r'^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+$', nombre):
            raise forms.ValidationError("El nombre solo puede contener letras y espacios.")
        return nombre

class FormSuscripcion(forms.Form):
    emailSus = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Tu correo electrónico'
        })
    )
