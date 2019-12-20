from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from alumnos import views

urlpatterns = [

    url('alumno', views.AlumnosList.as_view(), name = 'alumno'),
    url('alumno', views.AlumnosDetail.as_view(), name = 'alumno'),
    url('estado', views.SituacionList.as_view(), name = 'estado'),
    url('estado', views.SituacionDetail.as_view(), name = 'estado'),

]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])
