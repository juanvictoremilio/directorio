from django.db import models

# Create your models here.

class Doctor(models.Model):
    FEMENINO= 'FEM'
    MASCULINO = 'MASC'
    GENERO = [(FEMENINO, 'Femenino'), (MASCULINO, 'Masculino')] 

    doctor = models.CharField(max_length=200)
    speciality = models.CharField(max_length=200, verbose_name="Especialidad")
    languages = models.CharField(max_length=30, verbose_name="Idiomas")
    gender = models.CharField(max_length=50, choices=GENERO, verbose_name="Género")
    locations = models.CharField(max_length=200, verbose_name="Locaciones")
    phone = models.CharField(max_length=200, verbose_name="Teléfono")
    image = models.FileField(upload_to='doctores', verbose_name="Imagen")
    link = models.URLField(verbose_name="Dirección Web", null=True, blank=True)
    reference = models.TextField(verbose_name="Referencias")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "doctor"
        verbose_name_plural = "doctores"
        ordering = ["-created"]

    def __str__(self):
        return self.doctor

