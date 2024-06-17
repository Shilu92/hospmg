from django import forms
from .models import Patient, PatientUpdate, TreatmentPlan, Doctor, Appointment, Invoice, Report

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        
class PatientUpdateForm(forms.ModelForm):
    class Meta:
        model = PatientUpdate
        fields = '__all__'

class TreatmentPlanForm(forms.ModelForm):
    class Meta:
        model = TreatmentPlan
        fields = '__all__'

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = '__all__'
