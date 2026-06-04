from django.db import models
from django.contrib.auth.models import User


class Doctor(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    special = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Patient(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    mobile = models.CharField(null=True)
    contact = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date1 = models.DateField()
    Time1 = models.TimeField()



    def __str__(self):
        return self.doctor.name + " -- " + self.patient.name
