from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.parsers import MultiPartParser, FormParser

from main.models import Propiedad, Cliente, Comunas, Contacto, TiposPropiedades, EstadosPropiedades, OperacionesPropiedades, Suscripcion

from main.serializers import PropiedadSerializer, ClienteSerializer, ComunaSerializer, ContactoSerializer,TipoPropiedadSerializer, EstadoPropiedadSerializer,OperacionPropiedadSerializer, SuscripcionSerializer

from rest_framework.permissions import AllowAny, IsAdminUser

class PropiedadList(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAdminUser()]

    def get(self, request):
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
        serializer = PropiedadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)



class PropiedadDetail(APIView):

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAdminUser()]

    def get_object(self, slug):
        try:
            return Propiedad.objects.get(slug=slug)
        except Propiedad.DoesNotExist:
            raise Http404

    def get(self, request, slug):
        serializer = PropiedadSerializer(self.get_object(slug))
        return Response(serializer.data)

    def put(self, request, slug):
        serializer = PropiedadSerializer(
            self.get_object(slug),
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, slug):
        self.get_object(slug).delete()
        return Response(status=204)



class TipoPropiedadList(APIView):

    def get(self, request):
        serializer = TipoPropiedadSerializer(
            TiposPropiedades.objects.all(),
            many=True
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = TipoPropiedadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class TipoPropiedadDetail(APIView):

    def get_object(self, pk):
        try:
            return TiposPropiedades.objects.get(pk=pk)
        except TiposPropiedades.DoesNotExist:
            raise Http404

    def delete(self, request, pk):
        self.get_object(pk).delete()
        return Response(status=204)

class EstadoPropiedadList(APIView):

    def get(self, request):
        serializer = EstadoPropiedadSerializer(
            EstadosPropiedades.objects.all(),
            many=True
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = EstadoPropiedadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class EstadoPropiedadDetail(APIView):

    def get_object(self, pk):
        try:
            return EstadosPropiedades.objects.get(pk=pk)
        except EstadosPropiedades.DoesNotExist:
            raise Http404

    def delete(self, request, pk):
        self.get_object(pk).delete()
        return Response(status=204)
    

class OperacionPropiedadList(APIView):

    def get(self, request):
        serializer = OperacionPropiedadSerializer(
            OperacionesPropiedades.objects.all(),
            many=True
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = OperacionPropiedadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class OperacionPropiedadDetail(APIView):

    def get_object(self, pk):
        try:
            return OperacionesPropiedades.objects.get(pk=pk)
        except OperacionesPropiedades.DoesNotExist:
            raise Http404

    def delete(self, request, pk):
        self.get_object(pk).delete()
        return Response(status=204)


class ComunaList(APIView):

    def get(self, request):
        serializer = ComunaSerializer(
            Comunas.objects.all(),
            many=True
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = ComunaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)



class ComunaDetail(APIView):

    def get_object(self, pk):
        try:
            return Comunas.objects.get(pk=pk)
        except Comunas.DoesNotExist:
            raise Http404

    def delete(self, request, pk):
        self.get_object(pk).delete()
        return Response(status=204)


class ContactoList(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        serializer = ContactoSerializer(
            Contacto.objects.all(),
            many=True
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = ContactoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class ContactoDetail(APIView):

    def get_object(self, pk):
        try:
            return Contacto.objects.get(pk=pk)
        except Contacto.DoesNotExist:
            raise Http404

    def delete(self, request, pk):
        self.get_object(pk).delete()
        return Response(status=204)


class ClienteList(APIView):

    def get(self, request):
        serializer = ClienteSerializer(
            Cliente.objects.all(),
            many=True
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class ClienteDetail(APIView):

    def get_object(self, pk):
        try:
            return Cliente.objects.get(pk=pk)
        except Cliente.DoesNotExist:
            raise Http404

    def delete(self, request, pk):
        self.get_object(pk).delete()
        return Response(status=204)

class SuscripcionList(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        suscripciones = Suscripcion.objects.all()
        serializer = SuscripcionSerializer(suscripciones, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SuscripcionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

