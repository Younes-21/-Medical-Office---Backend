from rest_framework.serializers import ModelSerializer
from .models import *

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class PatientSerializer(ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class AppointmentSerializer(ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

class ScheduleSerializer(ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'
    
class MedicalFileSerializer(ModelSerializer):
    class Meta:
        model = MedicalFile
        fields = '__all__'