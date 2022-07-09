from django.urls import path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('users',UsersViewSet)
router.register('patients',PatientsViewSet)
router.register('schedules',SchedulesViewSet)
router.register('appointments',AppointmentsViewSet)
router.register('medicalfiles',MedicalFilesViewSet)
urlpatterns = router.urls