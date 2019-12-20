from rest_framework import serializers
from alumnos.models import Alumno
from alumnos.models import Situacion

class AlumnosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = '__all__'

class SituacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Situacion
        fields = '__all__'
