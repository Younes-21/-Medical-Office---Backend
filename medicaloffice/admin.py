from django.contrib import admin

from .models import Appointment, MedicalFile, Patient, Schedule, User
admin.site.register(User)
admin.site.register(Schedule)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(MedicalFile)