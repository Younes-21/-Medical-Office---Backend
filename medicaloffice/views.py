from re import U
from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *

class UsersViewSet(ModelViewSet):
    queryset=User.objects.all()
    serializer_class = UserSerializer

class PatientsViewSet(ModelViewSet):
    queryset=Patient.objects.all()
    serializer_class = PatientSerializer

class SchedulesViewSet(ModelViewSet):
    queryset=Schedule.objects.all()
    serializer_class = ScheduleSerializer

class AppointmentsViewSet(ModelViewSet):
    queryset=Appointment.objects.all()
    serializer_class = AppointmentSerializer

class MedicalFilesViewSet(ModelViewSet):
    queryset=MedicalFile.objects.all()
    serializer_class = MedicalFileSerializer
