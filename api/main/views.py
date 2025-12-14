from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.parsers import MultiPartParser, FormParser

from main.models import Propiedad, Cliente, Comunas, Contacto, TiposPropiedades, EstadosPropiedades, OperacionesPropiedades, Suscripcion


from main.serializers import PropiedadSerializer, ClienteSerializer, ComunaSerializer, ContactoSerializer,TipoPropiedadSerializer, EstadoPropiedadSerializer,OperacionPropiedadSerializer, SuscripcionSerializer

# Create your views here.
class PropiedadList(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request):
        propiedades = Propiedad.objects.all()
        serializer = PropiedadSerializer(propiedades, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PropiedadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PropiedadDetail(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def get_object(self, pk):
        try:
            return Propiedad.objects.get(pk=pk)
        except Propiedad.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        serializer = PropiedadSerializer(self.get_object(pk))
        return Response(serializer.data)

    def put(self, request, pk):
        serializer = PropiedadSerializer(
            self.get_object(pk),
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        self.get_object(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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

    def post(self, request):
        serializer = SuscripcionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
