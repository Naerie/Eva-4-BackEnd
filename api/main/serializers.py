from rest_framework import serializers
from main.models import (
    Propiedad, Cliente, Comunas, Contacto, TiposPropiedades, 
    EstadosPropiedades, OperacionesPropiedades, Suscripcion, Interes
)
import re


class PropiedadSerializer(serializers.ModelSerializer):
    """
    Serializer para la entidad Propiedad.
    Incluye validaciones personalizadas para superficie, estacionamiento y precio.
    """
    class Meta:
        model = Propiedad
        fields = '__all__'
        read_only_fields = ['fecha', 'slug']

    # VALIDACIONES PERSONALIZADAS
    def validate(self, data):
        """Validación a nivel de objeto para relaciones entre campos"""
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
        """Validación del campo precio"""
        try:
            valor = float(value)
        except (ValueError, TypeError):
            raise serializers.ValidationError("El precio debe ser un número válido.")

        if valor <= 0:
            raise serializers.ValidationError("El precio debe ser mayor a 0.")

        return value

    def validate_titulo(self, value):
        """Validación del título"""
        if len(value) < 3:
            raise serializers.ValidationError("El título debe tener al menos 3 caracteres.")
        if len(value) > 50:
            raise serializers.ValidationError("El título no puede exceder 50 caracteres.")
        return value

    def validate_descripcion(self, value):
        """Validación de la descripción"""
        if len(value) < 10:
            raise serializers.ValidationError("La descripción debe tener al menos 10 caracteres.")
        return value



class TipoPropiedadSerializer(serializers.ModelSerializer):
    """
    Serializer para la entidad TiposPropiedades.
    Valida que el tipo de propiedad sea único.
    """
    class Meta:
        model = TiposPropiedades
        fields = '__all__'

    def validate_tipoPropiedad(self, value):
        """Validación de unicidad del tipo de propiedad"""
        # Excluir el objeto actual en caso de actualización
        queryset = TiposPropiedades.objects.filter(tipoPropiedad=value)
        if self.instance:
            queryset = queryset.exclude(pk=self.instance.pk)
        
        if queryset.exists():
            raise serializers.ValidationError("Ya existe un tipo de propiedad con este nombre.")
        return value



class EstadoPropiedadSerializer(serializers.ModelSerializer):
    """
    Serializer para la entidad EstadosPropiedades.
    Valida que el estado sea único.
    """
    class Meta:
        model = EstadosPropiedades
        fields = '__all__'

    def validate_estado(self, value):
        """Validación de unicidad del estado"""
        queryset = EstadosPropiedades.objects.filter(estado=value)
        if self.instance:
            queryset = queryset.exclude(pk=self.instance.pk)
        
        if queryset.exists():
            raise serializers.ValidationError("Ya existe un estado con este nombre.")
        return value



class OperacionPropiedadSerializer(serializers.ModelSerializer):
    """
    Serializer para la entidad OperacionesPropiedades.
    Valida que la operación sea única.
    """
    class Meta:
        model = OperacionesPropiedades
        fields = '__all__'

    def validate_operacion(self, value):
        """Validación de unicidad de la operación"""
        queryset = OperacionesPropiedades.objects.filter(operacion=value)
        if self.instance:
            queryset = queryset.exclude(pk=self.instance.pk)
        
        if queryset.exists():
            raise serializers.ValidationError("Ya existe una operación con este nombre.")
        return value


class ComunaSerializer(serializers.ModelSerializer):
    """
    Serializer para la entidad Comunas.
    Valida que la comuna sea única.
    """
    class Meta:
        model = Comunas
        fields = '__all__'

    def validate_comuna(self, value):
        """Validación de unicidad de la comuna"""
        queryset = Comunas.objects.filter(comuna=value)
        if self.instance:
            queryset = queryset.exclude(pk=self.instance.pk)
        
        if queryset.exists():
            raise serializers.ValidationError("Ya existe una comuna con este nombre.")
        return value


class ContactoSerializer(serializers.ModelSerializer):
    """
    Serializer para la entidad Contacto.
    Incluye validaciones de nombre, email y teléfono.
    """
    class Meta:
        model = Contacto
        exclude = ['fecha']
        read_only_fields = ['fecha']

    def validate_nombre(self, value):
        """Validación del nombre - solo letras y espacios"""
        patron = r'^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+$'
        if not re.fullmatch(patron, value):
            raise serializers.ValidationError("El nombre solo puede contener letras y espacios.")
        if len(value) < 3:
            raise serializers.ValidationError("El nombre debe tener al menos 3 caracteres.")
        return value

    def validate_email(self, value):
        """Validación del email"""
        pat = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.fullmatch(pat, value):
            raise serializers.ValidationError("Dirección de correo inválida.")
        return value

    def validate_nTelefono(self, value):
        """Validación del teléfono"""
        # Acepta formato: +56912345678 o 912345678
        pat = r'^(\+\d{1,3})?\d{8,15}$'
        if not re.fullmatch(pat, value):
            raise serializers.ValidationError("Número de teléfono inválido. Use formato: +56912345678 o 912345678")
        return value



class ClienteSerializer(serializers.ModelSerializer):
    """
    Serializer para la entidad Cliente.
    Incluye validaciones de nombre, email y teléfono.
    """
    class Meta:
        model = Cliente
        exclude = ['fechaCliente']
        read_only_fields = ['fechaCliente']

    def validate_nombreCliente(self, value):
        """Validación del nombre del cliente"""
        patron = r'^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+$'
        if not re.fullmatch(patron, value):
            raise serializers.ValidationError("El nombre solo puede contener letras y espacios.")
        if len(value) < 3:
            raise serializers.ValidationError("El nombre debe tener al menos 3 caracteres.")
        return value

    def validate_emailCliente(self, value):
        """Validación del email del cliente"""
        pat = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.fullmatch(pat, value):
            raise serializers.ValidationError("Dirección de correo inválida.")
        return value

    def validate_nTelefonoCliente(self, value):
        """Validación del teléfono del cliente"""
        pat = r'^(\+\d{1,3})?\d{8,15}$'
        if not re.fullmatch(pat, value):
            raise serializers.ValidationError("Número de teléfono inválido. Use formato: +56912345678 o 912345678")
        return value


class SuscripcionSerializer(serializers.ModelSerializer):
    """
    Serializer para la entidad Suscripcion.
    Valida que el email sea único y tenga formato válido.
    """
    class Meta:
        model = Suscripcion
        fields = ['id', 'emailSus', 'fechaSus', 'estadoSus']
        read_only_fields = ['fechaSus']

    def validate_emailSus(self, value):
        """Validación del email de suscripción"""
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.fullmatch(patron, value):
            raise serializers.ValidationError("Dirección de correo inválida.")

        # Excluir el objeto actual en caso de actualización
        queryset = Suscripcion.objects.filter(emailSus=value)
        if self.instance:
            queryset = queryset.exclude(pk=self.instance.pk)

        if queryset.exists():
            raise serializers.ValidationError("Este email ya está suscrito.")

        return value


class InteresSerializer(serializers.ModelSerializer):
    """
    Serializer para la entidad Interes.
    Permite crear y gestionar los intereses de clientes en propiedades.
    Valida que no haya intereses duplicados.
    """
    class Meta:
        model = Interes
        fields = '__all__'
        read_only_fields = ['creado']

    def validate(self, data):
        """
        Validación personalizada para evitar intereses duplicados.
        """
        cliente = data.get('cliente')
        propiedad = data.get('propiedad')
        
        if cliente and propiedad:
            # Excluir el objeto actual en caso de actualización
            queryset = Interes.objects.filter(cliente=cliente, propiedad=propiedad)
            if self.instance:
                queryset = queryset.exclude(pk=self.instance.pk)
            
            if queryset.exists():
                raise serializers.ValidationError(
                    "Este cliente ya tiene un interes registrado en esta propiedad."
                )
        
        return data

    def validate_cliente(self, value):
        """Validación de que el cliente exista"""
        if not value:
            raise serializers.ValidationError("El cliente es requerido.")
        return value

    def validate_propiedad(self, value):
        """Validación de que la propiedad exista"""
        if not value:
            raise serializers.ValidationError("La propiedad es requerida.")
        return value