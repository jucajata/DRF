from django.urls import path

from .views import (
    list_patients, detail_patient, 
    ListPatients1View, DetailPatients1View,
    ListPatientsView, DetailPatientsView
)

urlpatterns = [
    path("patients_func/", list_patients),
    path("patients_class/", ListPatients1View.as_view()),
    path("patients/", ListPatientsView.as_view()),
    path("patients_func/<int:pk>/", detail_patient),
    path("patients_class/<int:pk>/", DetailPatients1View.as_view()),
    path("patients/<int:pk>/", DetailPatientsView.as_view()),
]