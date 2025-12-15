from django import forms

class FormRegistrarP(forms.Form):
    """
    Formulario para registrar/actualizar propiedades.
    Incluye validaciones personalizadas.
    """
    titulo = forms.CharField(max_length=50)
    descripcion = forms.CharField(widget=forms.Textarea)
    thumb = forms.ImageField(required=True)

    nHabitaciones = forms.IntegerField()
    nBanos = forms.IntegerField()

    superficie = forms.FloatField(required=False)
    superficieConstruida = forms.FloatField(required=False)

    ubicacion = forms.CharField(max_length=50)
    precio = forms.DecimalField(min_value=1)
    moneda = forms.ChoiceField(choices=[('UF', 'UF'), ('CLP', '$')])

    estacionamiento = forms.BooleanField(required=False)
    nEstacionamientos = forms.IntegerField(required=False)

    piscina = forms.BooleanField(required=False)
    conserje = forms.BooleanField(required=False)
    logia = forms.BooleanField(required=False)
    amoblado = forms.BooleanField(required=False)

    comuna = forms.ChoiceField(required=False)
    tipo_propiedad = forms.ChoiceField(required=False)
    operacion = forms.ChoiceField(required=False)
    estado = forms.ChoiceField(required=False)

    def clean(self):
        cleaned = super().clean()

        sup = cleaned.get('superficie')
        sup_c = cleaned.get('superficieConstruida')

        if sup is not None and sup_c is not None and sup_c > sup:
            self.add_error(
                'superficieConstruida',
                "La superficie construida no puede ser mayor a la total."
            )

        est = cleaned.get('estacionamiento')
        n_est = cleaned.get('nEstacionamientos')

        if not est and n_est is not None and n_est > 0:
            self.add_error(
                'nEstacionamientos',
                "No puede indicar estacionamientos si no marca la opción."
            )

        return cleaned


# ============================================
# FORMULARIOS PARA GESTIÓN DE CATÁLOGOS
# ============================================

class FormTiposPropiedades(forms.Form):
    """
    Formulario para crear/actualizar tipos de propiedad.
    Ejemplo: Departamento, Casa, Oficina, etc.
    """
    tipoPropiedad = forms.CharField(
        max_length=50,
        label="Tipo de Propiedad",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej: Departamento, Casa, Oficina'
        })
    )

    def clean_tipoPropiedad(self):
        """Validación del campo tipoPropiedad"""
        value = self.cleaned_data.get('tipoPropiedad')
        if not value:
            raise forms.ValidationError("Este campo es requerido.")
        if len(value) < 3:
            raise forms.ValidationError("Debe tener al menos 3 caracteres.")
        return value


class FormEstadosPropiedades(forms.Form):
    """
    Formulario para crear/actualizar estados de propiedad.
    Ejemplo: Disponible, Vendido, Alquilado, etc.
    """
    estado = forms.CharField(
        max_length=50,
        label="Estado de Propiedad",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej: Disponible, Vendido, Alquilado'
        })
    )

    def clean_estado(self):
        """Validación del campo estado"""
        value = self.cleaned_data.get('estado')
        if not value:
            raise forms.ValidationError("Este campo es requerido.")
        if len(value) < 3:
            raise forms.ValidationError("Debe tener al menos 3 caracteres.")
        return value


class FormOperacionesPropiedades(forms.Form):
    """
    Formulario para crear/actualizar operaciones de propiedad.
    Ejemplo: Venta, Arriendo, Permuta, etc.
    """
    operacion = forms.CharField(
        max_length=50,
        label="Tipo de Operación",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej: Venta, Arriendo, Permuta'
        })
    )

    def clean_operacion(self):
        """Validación del campo operación"""
        value = self.cleaned_data.get('operacion')
        if not value:
            raise forms.ValidationError("Este campo es requerido.")
        if len(value) < 3:
            raise forms.ValidationError("Debe tener al menos 3 caracteres.")
        return value


class FormComunas(forms.Form):
    """
    Formulario para crear/actualizar comunas.
    Ejemplo: Santiago, Providencia, La Florida, etc.
    """
    comuna = forms.CharField(
        max_length=50,
        label="Comuna",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej: Santiago, Providencia, La Florida'
        })
    )

    def clean_comuna(self):
        """Validación del campo comuna"""
        value = self.cleaned_data.get('comuna')
        if not value:
            raise forms.ValidationError("Este campo es requerido.")
        if len(value) < 3:
            raise forms.ValidationError("Debe tener al menos 3 caracteres.")
        return value


# ============================================
# FORMULARIOS PARA USUARIO
# ============================================

class FormSuscripcion(forms.Form):
    """
    Formulario para suscribirse a la newsletter.
    """
    emailSus = forms.EmailField(
        label="Correo Electrónico",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'tu@email.com'
        })
    )


class FormContacto(forms.Form):
    """
    Formulario para enviar mensajes de contacto.
    """
    nombre = forms.CharField(
        max_length=50,
        label="Nombre",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Tu nombre'
        })
    )
    
    email = forms.EmailField(
        label="Correo Electrónico",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'tu@email.com'
        })
    )
    
    nTelefono = forms.CharField(
        max_length=15,
        label="Teléfono",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '+56912345678 o 912345678'
        })
    )
    
    mensaje = forms.CharField(
        label="Mensaje",
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Tu mensaje aquí...',
            'rows': 5
        })
    )


class FormCliente(forms.Form):
    """
    Formulario para registrar clientes interesados.
    """
    nombreCliente = forms.CharField(
        max_length=50,
        label="Nombre",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Tu nombre'
        })
    )
    
    emailCliente = forms.EmailField(
        label="Correo Electrónico",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'tu@email.com'
        })
    )
    
    nTelefonoCliente = forms.CharField(
        max_length=15,
        label="Teléfono",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '+56912345678 o 912345678'
        })
    )