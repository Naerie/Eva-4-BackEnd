from django import forms

class FormRegistrarP(forms.Form):

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

    # IDs que vienen de la API
    comuna = forms.IntegerField()
    tipo_propiedad = forms.IntegerField()
    operacion = forms.IntegerField()
    estado = forms.IntegerField()

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





