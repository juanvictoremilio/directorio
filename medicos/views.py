from django.shortcuts import render
from .models import Doctor
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.
class DoctorListView(ListView):
    model = Doctor
    template_name = 'doctor_list.html'

class DoctorDetailView(DetailView):
    model = Doctor
