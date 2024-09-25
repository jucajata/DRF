from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from doctors.models import Doctor
from patients.models import Patient

# Create your tests here.
class DoctorViewSetTests(TestCase):

    def setUp(self):
        self.patient = Patient.objects.create(
            first_name="Juan",
            last_name="Jaramillo",
            date_of_birth="1995-05-24",
            contact_number="3155177752",
            email="jcjt95@gmail.com",
            address="La Marina",
            medical_history="Ninguna",
        )
        self.doctor = Doctor.objects.create(
            first_name="Erika",
            last_name="Valencia",
            qualification="Profesional",
            contact_number="3163473329",
            email="erikavalval@gmail.com",
            address="La Marina",
            biography="Médica profesional",
            is_on_vacation=False,
        )
        self.client = APIClient()

    def test_list_should_return_403(self):
        url = reverse(
            "doctor-appointments", 
            kwargs={"pk": self.doctor.id}
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

