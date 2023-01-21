from django.urls import path
from . import views
from .views import (DoctorListView, DoctorDetailView)

app_name = "medicos"


medicos_patterns = ([
    path('', DoctorListView.as_view(), name='doctores'),
    path('<int:pk>/<slug:paciente_slug>/', DoctorDetailView.as_view(), name='doctor') 
   
   
], 'medicos')