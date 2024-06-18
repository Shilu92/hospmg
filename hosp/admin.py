from django.contrib import admin
from . models import Patient, PatientUpdate, TreatmentPlan, Doctor, Appointment, Invoice, Report

# Register your models here.


admin.site.register(Patient)
admin.site.register(PatientUpdate)
admin.site.register(TreatmentPlan)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Invoice)
admin.site.register(Report)