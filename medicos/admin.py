from django.contrib import admin
from .models import Doctor

# Register your models here.

class DoctorAdmin(admin.ModelAdmin):
    list_display = ['doctor', 'speciality', 'languages', 'gender', 'phone', 'created', 'updated']
    readonly_fields = ('created', 'updated')
    search_fields = ('doctor', 'speciality', 'gender', 'locations')
    list_filter = ['speciality']
    
	
	


admin.site.register(Doctor, DoctorAdmin)
