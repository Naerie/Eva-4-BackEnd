from rest_framework import serializers
from main.models import Propiedad
class propiedadesSerializer(serializers.ModelSerializer):
    class Meta:
        models = Propiedad
        fields = "__all__"