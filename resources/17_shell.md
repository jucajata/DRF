(.venv) (base) erika@debian12:~/dev/DRF$ python manage.py shell
Python 3.12.4 | packaged by Anaconda, Inc. | (main, Jun 18 2024, 15:12:24) [GCC 11.2.0]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.27.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from datetime import date, time

In [2]: from doctors.models import Doctor

In [3]: from patients.models import Patient

In [4]: from bookings.models import Appointment

In [5]: patient = Patient.objects.get(id=3)

In [6]: patient
Out[6]: <Patient: Patient object (3)>

In [7]: doctor = Doctor.objects.first()

In [8]: doctor
Out[8]: <Doctor: Doctor object (1)>

In [9]: Appointment.objects.create(
   ...:     patient=patient,
   ...:     doctor=doctor,
   ...:     appointment_date=date(2022,12,5),
   ...:     appointment_time=time(9,0),
   ...:     notes="Ejemplo",
   ...:     status="HECHA")
Out[9]: <Appointment: Appointment object (1)>