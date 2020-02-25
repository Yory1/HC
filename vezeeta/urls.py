from django.urls import path
from . import views



app_name = 'vezeeta'

urlpatterns = [
# Doctors URLs
    path('doctor_details/<NN>/', views.Doctor_Details, name='doctor_details'),
    path('clinic_details/<id>/', views.Clinic_Details, name='clinic_details'),
]
