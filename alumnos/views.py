from rest_framework import generics
from alumnos.models import Alumno
from alumnos.serializers import AlumnosSerializer
from alumnos.models import Situacion
from alumnos.serializers import SituacionSerializer
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response


def promedio(Alumno): #calcula el promedio del alumno
    prom = (float(Alumno["nota1"]) + float(Alumno["nota2"]) + float(Alumno["nota3"]) + float(Alumno["nota4"]))/4
    return prom

def estado(prom):#calcula el promedioestado del alumno segun su promedio
    if (prom > 3.95):
        estado = "Aprobado"
        return estado
    else:
        estado = "Reprobado"
        return estado

def listaestados(alumno): #guarda la situacion correspondiente al alumno
    prom = promedio(alumno)
    a = Alumno.objects.get(id=alumno["id"])
    e = Situacion(promedio=prom,estado=estado(prom),alumno=a)
    e.save()
#Vistas del alumno, ingresar y mostrar
class AlumnosList(generics.ListCreateAPIView):
    queryset = Alumno.objects.all()
    serializer_class = AlumnosSerializer
    lista = list(Alumno.objects.all())
#al momento de ingresar el alumno guarda su situacion
    def post(self, request, format=None):
        serializer = AlumnosSerializer(data=request.data)
        if serializer.is_valid():#valida la informacion segun el serializer
            serializer.save()#guarda el alumno en la base de datos
            listaestados(serializer.data)#guarda la situacion
            return Response(serializer.data)
        else:
            return Response("Error {}".format(serializer.errors))

class AlumnosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Situacion.objects.all()
    serializer_class = SituacionSerializer

#Vistas de la situacion del alumno, ingresar y mostrar
class SituacionList(generics.ListCreateAPIView):
    queryset = Situacion.objects.all()
    serializer_class = SituacionSerializer

class SituacionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Situacion.objects.all()
    serializer_class = SituacionSerializer
