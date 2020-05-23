from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "appointment"

urlpatterns = [
    path("appointments/p/", views.AppointmentsForAPatientView.as_view(), name="patient-appointments"),
    path("appointments/d/", views.AppointmentsForADoctorView.as_view(), name="doctor-appointments"),
    path("medHistory/", views.MedicalHistoryView.as_view(), name="med-history"),
    path("prescriptions/", views.PrescriptionListView.as_view(), name="doc-prescriptions"),
    path("prescription/create", views.PrescriptionCreateView, name="doc-prescriptions-create"),
]