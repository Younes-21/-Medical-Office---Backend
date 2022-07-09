from django.db import models
from django.core.validators import MinValueValidator
from datetime import datetime

class User(models.Model):
    def __str__(self):
        return f'{self.firstName} {self.lastName}'
    firstName = models.fields.CharField(max_length=20)
    lastName = models.fields.CharField(max_length=20)
    cin = models.fields.CharField(max_length=20)
    phone = models.fields.CharField(max_length=20)
    email = models.fields.EmailField(max_length=100)
    password = models.fields.CharField(max_length=100)
    address = models.fields.CharField(max_length=500)
    salary = models.fields.FloatField(
        validators=[MinValueValidator(0)],
        null=True, blank=True)
    beginDate = models.fields.DateField()
    endDate = models.fields.DateField(null=True , blank=True)

    role = models.fields.CharField(max_length=20)

class Schedule(models.Model):
    def __str__(self):
        return f'{self.user.firstName} {self.user.lastName}'
    date = models.DateTimeField()
    availability = models.BooleanField()
    user = models.ForeignKey(User, null=True , on_delete=models.CASCADE)

class Patient(models.Model):
    def __str__(self):
        return f'{self.firstName} {self.lastName}'
    firstName = models.fields.CharField(max_length=20)
    lastName = models.fields.CharField(max_length=20)
    cin = models.fields.CharField(max_length=20)
    phone = models.fields.CharField(max_length=20)
    email = models.fields.EmailField(max_length=100)
    password = models.fields.CharField(max_length=100)
    address = models.fields.CharField(max_length=500)
    dateBirth = models.fields.DateField(null=False)

class Appointment(models.Model):
    def __str__(self):
        return f'{self.user.firstName} {self.user.lastName}'
    date = models.fields.DateTimeField(default=datetime.now())
    paymentStatus = models.fields.BooleanField(default=False)
    price = models.fields.FloatField(
        validators=[MinValueValidator(0)])
    totalPaid = models.fields.FloatField(
        validators=[MinValueValidator(0)])
    reason = models.fields.CharField(max_length=1000, null=True , blank=True)
    prescription = models.fields.CharField(max_length=1000)
    patient = models.ForeignKey(Patient, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True , on_delete=models.CASCADE)

class MedicalFile(models.Model):
    def __str__(self):
        return f'{self.patient.firstName} {self.patient.lastName}'
    date = models.fields.DateTimeField(null=False)
    bloodGroup = models.fields.CharField(max_length=5, null=False)
    height = models.fields.FloatField(
        validators=[MinValueValidator(0)],
        null=False)
    weight = models.fields.FloatField(
        validators=[MinValueValidator(0)],
        null=False)
    allergy = models.fields.CharField(max_length=2000, null=True , blank=True)
    vaccination = models.fields.CharField(max_length=2000, null =True , blank=True)
    healthInsurance = models.fields.CharField(max_length=500,null=True , blank=True)
    patient = models.ForeignKey(Patient, null=True, on_delete=models.CASCADE)


