from django.db import models
from .validacion import valor_nota
# Create your models here.
class Alumno(models.Model):

    nombre = models.CharField(max_length=25, blank=False, default='')
    nota1 = models.DecimalField(max_digits=3, decimal_places=2, blank=False, validators=[valor_nota])
    nota2 = models.DecimalField(max_digits=3, decimal_places=2, blank=False, validators=[valor_nota])
    nota3 = models.DecimalField(max_digits=3, decimal_places=2, blank=False, validators=[valor_nota])
    nota4 = models.DecimalField(max_digits=3, decimal_places=2, blank=False, validators=[valor_nota])

    def __str__(self):
        return self.nombre



class Situacion(models.Model):
    promedio = models.DecimalField(max_digits=3, decimal_places=2, blank=False)
    estado = models.CharField(max_length=15, blank=True, default='')
#    nombre = models.CharField(max_length=25, blank=True, default='')
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)

    def __str__(self):
        return self.promedio
