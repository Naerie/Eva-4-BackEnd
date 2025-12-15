from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.parsers import MultiPartParser, FormParser

from main.models import (
    Propiedad, Cliente, Comunas, Contacto, TiposPropiedades, 
    EstadosPropiedades, OperacionesPropiedades, Suscripcion, Interes
)

from main.serializers import (
    PropiedadSerializer, ClienteSerializer, ComunaSerializer, ContactoSerializer,
    TipoPropiedadSerializer, EstadoPropiedadSerializer, OperacionPropiedadSerializer, 
    SuscripcionSerializer, InteresSerializer
)

from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated


# ============================================
# PROPIEDADES - CRUD COMPLETO
# ============================================
class PropiedadList(APIView):
    """
    API endpoint para listar y crear propiedades.
    GET: Obtiene todas las propiedades con filtros opcionales
    POST: Crea una nueva propiedad (requiere autenticación de admin)
    """
    parser_classes = [MultiPartParser, FormParser]

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAdminUser()]

    def get(self, request):
        """
        Obtiene todas las propiedades.
        Soporta filtros por: operacion, tipo_propiedad, comuna
        """
        propiedades = Propiedad.objects.all()

        operacion = request.GET.get('operacion')
        tipo = request.GET.get('tipo_propiedad')
        comuna = request.GET.get('comuna')

        if operacion:
            propiedades = propiedades.filter(operacion_id=operacion)
        if tipo:
            propiedades = propiedades.filter(tipo_propiedad_id=tipo)
        if comuna:
            propiedades = propiedades.filter(comuna_id=comuna)

        serializer = PropiedadSerializer(propiedades, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Crea una nueva propiedad.
        Requiere autenticación de administrador.
        """
        serializer = PropiedadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PropiedadDetail(APIView):
    """
    API endpoint para obtener, actualizar y eliminar una propiedad específica.
    """
    parser_classes = [MultiPartParser, FormParser]

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAdminUser()]

    def get_object(self, slug):
        try:
            return Propiedad.objects.get(slug=slug)
        except Propiedad.DoesNotExist:
            raise Http404("Propiedad no encontrada")

    def get(self, request, slug):
        """Obtiene los detalles de una propiedad específica"""
        serializer = PropiedadSerializer(self.get_object(slug))
        return Response(serializer.data)

    def put(self, request, slug):
        """Actualiza una propiedad existente"""
        serializer = PropiedadSerializer(
            self.get_object(slug),
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug):
        """Elimina una propiedad"""
        self.get_object(slug).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ============================================
# TIPOS DE PROPIEDAD - CRUD COMPLETO
# ============================================
class TipoPropiedadList(APIView):
    """
    API endpoint para listar y crear tipos de propiedad.
    """
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAdminUser()]

    def get(self, request):
        """Obtiene todos los tipos de propiedad"""
        serializer = TipoPropiedadSerializer(
            TiposPropiedades.objects.all(),
            many=True
        )
        return Response(serializer.data)

    def post(self, request):
        """Crea un nuevo tipo de propiedad"""
        serializer = TipoPropiedadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TipoPropiedadDetail(APIView):
    """
    API endpoint para obtener, actualizar y eliminar un tipo de propiedad.
    """
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAdminUser()]

    def get_object(self, pk):
        try:
            return TiposPropiedades.objects.get(pk=pk)
        except TiposPropiedades.DoesNotExist:
            raise Http404("Tipo de propiedad no encontrado")

    def get(self, request, pk):
        """Obtiene los detalles de un tipo de propiedad"""
        serializer = TipoPropiedadSerializer(self.get_object(pk))
        return Response(serializer.data)

    def put(self, request, pk):
        """Actualiza un tipo de propiedad"""
        serializer = TipoPropiedadSerializer(
            self.get_object(pk),
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Elimina un tipo de propiedad"""
        self.get_object(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ============================================
# ESTADOS DE PROPIEDAD - CRUD COMPLETO
# ============================================
class EstadoPropiedadList(APIView):
    """
    API endpoint para listar y crear estados de propiedad.
    """
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAdminUser()]

    def get(self, request):
        """Obtiene todos los estados de propiedad"""
        serializer = EstadoPropiedadSerializer(
            EstadosPropiedades.objects.all(),
            many=True
        )
        return Response(serializer.data)

    def post(self, request):
        """Crea un nuevo estado de propiedad"""
        serializer = EstadoPropiedadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EstadoPropiedadDetail(APIView):
    """
    API endpoint para obtener, actualizar y eliminar un estado de propiedad.
    """
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAdminUser()]

    def get_object(self, pk):
        try:
            return EstadosPropiedades.objects.get(pk=pk)
        except EstadosPropiedades.DoesNotExist:
            raise Http404("Estado de propiedad no encontrado")

    def get(self, request, pk):
        """Obtiene los detalles de un estado de propiedad"""
        serializer = EstadoPropiedadSerializer(self.get_object(pk))
        return Response(serializer.data)

    def put(self, request, pk):
        """Actualiza un estado de propiedad"""
        serializer = EstadoPropiedadSerializer(
            self.get_object(pk),
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Elimina un estado de propiedad"""
        self.get_object(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ============================================
# OPERACIONES DE PROPIEDAD - CRUD COMPLETO
# ============================================
class OperacionPropiedadList(APIView):
    """
    API endpoint para listar y crear operaciones de propiedad.
    """
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAdminUser()]

    def get(self, request):
        """Obtiene todas las operaciones de propiedad"""
        serializer = OperacionPropiedadSerializer(
            OperacionesPropiedades.objects.all(),
            many=True
        )
        return Response(serializer.data)

    def post(self, request):
        """Crea una nueva operación de propiedad"""
        serializer = OperacionPropiedadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OperacionPropiedadDetail(APIView):
    """
    API endpoint para obtener, actualizar y eliminar una operación de propiedad.
    """
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAdminUser()]

    def get_object(self, pk):
        try:
            return OperacionesPropiedades.objects.get(pk=pk)
        except OperacionesPropiedades.DoesNotExist:
            raise Http404("Operación de propiedad no encontrada")

    def get(self, request, pk):
        """Obtiene los detalles de una operación de propiedad"""
        serializer = OperacionPropiedadSerializer(self.get_object(pk))
        return Response(serializer.data)

    def put(self, request, pk):
        """Actualiza una operación de propiedad"""
        serializer = OperacionPropiedadSerializer(
            self.get_object(pk),
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Elimina una operación de propiedad"""
        self.get_object(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ============================================
# COMUNAS - CRUD COMPLETO
# ============================================
class ComunaList(APIView):
    """
    API endpoint para listar y crear comunas.
    """
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAdminUser()]

    def get(self, request):
        """Obtiene todas las comunas"""
        serializer = ComunaSerializer(
            Comunas.objects.all(),
            many=True
        )
        return Response(serializer.data)

    def post(self, request):
        """Crea una nueva comuna"""
        serializer = ComunaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ComunaDetail(APIView):
    """
    API endpoint para obtener, actualizar y eliminar una comuna.
    """
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAdminUser()]

    def get_object(self, pk):
        try:
            return Comunas.objects.get(pk=pk)
        except Comunas.DoesNotExist:
            raise Http404("Comuna no encontrada")

    def get(self, request, pk):
        """Obtiene los detalles de una comuna"""
        serializer = ComunaSerializer(self.get_object(pk))
        return Response(serializer.data)

    def put(self, request, pk):
        """Actualiza una comuna"""
        serializer = ComunaSerializer(
            self.get_object(pk),
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Elimina una comuna"""
        self.get_object(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ============================================
# CONTACTOS - CRUD COMPLETO
# ============================================
class ContactoList(APIView):
    """
    API endpoint para listar y crear contactos.
    """
    permission_classes = [AllowAny]

    def get(self, request):
        """Obtiene todos los contactos"""
        serializer = ContactoSerializer(
            Contacto.objects.all(),
            many=True
        )
        return Response(serializer.data)

    def post(self, request):
        """Crea un nuevo contacto"""
        serializer = ContactoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContactoDetail(APIView):
    """
    API endpoint para obtener, actualizar y eliminar un contacto.
    """
    permission_classes = [AllowAny]

    def get_object(self, pk):
        try:
            return Contacto.objects.get(pk=pk)
        except Contacto.DoesNotExist:
            raise Http404("Contacto no encontrado")

    def get(self, request, pk):
        """Obtiene los detalles de un contacto"""
        serializer = ContactoSerializer(self.get_object(pk))
        return Response(serializer.data)

    def put(self, request, pk):
        """Actualiza un contacto"""
        serializer = ContactoSerializer(
            self.get_object(pk),
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Elimina un contacto"""
        self.get_object(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ============================================
# CLIENTES - CRUD COMPLETO
# ============================================
class ClienteList(APIView):
    """
    API endpoint para listar y crear clientes.
    """
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAdminUser()]

    def get(self, request):
        """Obtiene todos los clientes"""
        serializer = ClienteSerializer(
            Cliente.objects.all(),
            many=True
        )
        return Response(serializer.data)

    def post(self, request):
        """Crea un nuevo cliente"""
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClienteDetail(APIView):
    """
    API endpoint para obtener, actualizar y eliminar un cliente.
    """
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAdminUser()]

    def get_object(self, pk):
        try:
            return Cliente.objects.get(pk=pk)
        except Cliente.DoesNotExist:
            raise Http404("Cliente no encontrado")

    def get(self, request, pk):
        """Obtiene los detalles de un cliente"""
        serializer = ClienteSerializer(self.get_object(pk))
        return Response(serializer.data)

    def put(self, request, pk):
        """Actualiza un cliente"""
        serializer = ClienteSerializer(
            self.get_object(pk),
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Elimina un cliente"""
        self.get_object(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ============================================
# SUSCRIPCIONES - CRUD COMPLETO
# ============================================
class SuscripcionList(APIView):
    """
    API endpoint para listar y crear suscripciones.
    """
    permission_classes = [AllowAny]

    def get(self, request):
        """Obtiene todas las suscripciones"""
        serializer = SuscripcionSerializer(
            Suscripcion.objects.all(),
            many=True
        )
        return Response(serializer.data)

    def post(self, request):
        """Crea una nueva suscripción"""
        serializer = SuscripcionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SuscripcionDetail(APIView):
    """
    API endpoint para obtener, actualizar y eliminar una suscripción.
    """
    permission_classes = [AllowAny]

    def get_object(self, pk):
        try:
            return Suscripcion.objects.get(pk=pk)
        except Suscripcion.DoesNotExist:
            raise Http404("Suscripción no encontrada")

    def get(self, request, pk):
        """Obtiene los detalles de una suscripción"""
        serializer = SuscripcionSerializer(self.get_object(pk))
        return Response(serializer.data)

    def put(self, request, pk):
        """Actualiza una suscripción"""
        serializer = SuscripcionSerializer(
            self.get_object(pk),
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Elimina una suscripción"""
        self.get_object(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ============================================
# INTERESES - CRUD COMPLETO
# ============================================
class InteresList(APIView):
    """
    API endpoint para listar y crear intereses de clientes en propiedades.
    """
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]

    def get(self, request):
        """Obtiene todos los intereses registrados"""
        serializer = InteresSerializer(
            Interes.objects.all(),
            many=True
        )
        return Response(serializer.data)

    def post(self, request):
        """Crea un nuevo interes"""
        serializer = InteresSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InteresDetail(APIView):
    """
    API endpoint para obtener, actualizar y eliminar un interes específico.
    """
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]

    def get_object(self, pk):
        try:
            return Interes.objects.get(pk=pk)
        except Interes.DoesNotExist:
            raise Http404("Interes no encontrado")

    def get(self, request, pk):
        """Obtiene los detalles de un interes"""
        serializer = InteresSerializer(self.get_object(pk))
        return Response(serializer.data)

    def put(self, request, pk):
        """Actualiza un interes"""
        serializer = InteresSerializer(
            self.get_object(pk),
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Elimina un interes"""
        self.get_object(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
