from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    name = models.CharField(max_length = 50,null=True,blank = True )
    age = models.IntegerField(null=True, blank = True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    medical_history = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.user.get_full_name()


class PatientUpdate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE ,default = 1)
    name = models.CharField(max_length = 50,null=True,blank = True )
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    medical_history = models.TextField(blank=True, null=True)
    allergies = models.TextField(blank=True, null=True)
    ongoing_medications = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.user.get_full_name()


class TreatmentPlan(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    progress = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"TreatmentPlan for {self.patient} from {self.start_date} to {self.end_date}"
    

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default=1)
    first_name = models.CharField(max_length = 50,null=True,blank = True )
    last_name = models.CharField(max_length = 50,null=True,blank = True )
    specialization = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, default=1)
    availability = models.TextField()  # e.g., "Mon-Fri: 9am-5pm"
    
    def __str__(self):
        return self.user.get_full_name()

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=[('Scheduled', 'Scheduled'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')])

    def __str__(self):
        return f"{self.patient} with {self.doctor} on {self.date}"

class Invoice(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Invoice {self.id} for {self.patient}"

class Report(models.Model):
    report_type = models.CharField(max_length=50)
    generated_on = models.DateTimeField(auto_now_add=True)
    data = models.JSONField()

    def __str__(self):
        return f"{self.report_type} on {self.generated_on}"