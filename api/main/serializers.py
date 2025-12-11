from rest_framework import serializers
from main.models import Propiedad, Cliente, Comunas, Contacto, TiposPropiedades, EstadosPropiedades, OperacionesPropiedades, Suscripcion
import re



class PropiedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propiedad
        fields = '__all__'

    # VALIDACIONES PERSONALIZADAS
    def validate(self, data):
        superficie = data.get('superficie')
        superficie_construida = data.get('superficieConstruida')

        if superficie and superficie_construida:
            if superficie_construida > superficie:
                raise serializers.ValidationError({
                    'superficieConstruida': "La superficie construida no puede ser mayor que la superficie total."
                })

        estacionamiento = data.get('estacionamiento')
        n_est = data.get('nEstacionamientos')

        if not estacionamiento and n_est and n_est > 0:
            raise serializers.ValidationError({
                'nEstacionamientos': "No puede indicar número de estacionamientos si no selecciona 'Estacionamiento'."
            })

        return data

    def validate_precio(self, value):
        try:
            valor = float(value)
        except:
            raise serializers.ValidationError("El precio debe ser un número válido.")

        if valor <= 0:
            raise serializers.ValidationError("El precio debe ser mayor a 0.")

        return value


class TipoPropiedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TiposPropiedades
        fields = '__all__'

    def validate_tipoPropiedad(self, value):
        if TiposPropiedades.objects.filter(tipoPropiedad=value).exists():
            raise serializers.ValidationError("Ya existe en la base de datos.")
        return value


class EstadoPropiedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadosPropiedades
        fields = '__all__'

    def validate_estado(self, value):
        if EstadosPropiedades.objects.filter(estado=value).exists():
            raise serializers.ValidationError("Ese registro ya existe en la base de datos.")
        return value


class OperacionPropiedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperacionesPropiedades
        fields = '__all__'

    def validate_operacion(self, value):
        if OperacionesPropiedades.objects.filter(operacion=value).exists():
            raise serializers.ValidationError("Ese registro ya existe en la base de datos.")
        return value


class ComunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comunas
        fields = '__all__'

    def validate_comuna(self, value):
        if Comunas.objects.filter(comuna=value).exists():
            raise serializers.ValidationError("Ese registro ya existe en la base de datos.")
        return value


class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        exclude = ['fecha']

    def validate_nombre(self, value):
        patron = r'^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+$'
        if not re.fullmatch(patron, value):
            raise serializers.ValidationError("El nombre solo puede contener letras y espacios.")
        return value

    def validate_email(self, value):
        pat = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.fullmatch(pat, value):
            raise serializers.ValidationError("Dirección de correo inválida.")
        return value

    def validate_nTelefono(self, value):
        pat = r'^\+\d{1,3}\d{10}$'
        if not re.fullmatch(pat, value):
            raise serializers.ValidationError("Número de teléfono inválido.")
        return value


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        exclude = ['fechaCliente']

    def validate_nombreCliente(self, value):
        patron = r'^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+$'
        if not re.fullmatch(patron, value):
            raise serializers.ValidationError("El nombre solo puede contener letras y espacios.")
        return value

    def validate_emailCliente(self, value):
        pat = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.fullmatch(pat, value):
            raise serializers.ValidationError("Dirección de correo inválida.")
        return value

    def validate_nTelefonoCliente(self, value):
        pat = r'^\+\d{1,3}\d{10}$'
        if not re.fullmatch(pat, value):
            raise serializers.ValidationError("Número de teléfono inválido.")
        return value


class SuscripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suscripcion
        fields = ['emailSus']

    def validate_emailSus(self, value):
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.fullmatch(patron, value):
            raise serializers.ValidationError("Dirección de correo inválida.")

        if Suscripcion.objects.filter(emailSus=value).exists():
            raise serializers.ValidationError("Ya estás suscrito.")

        return value
