(.venv) (base) erika@debian12:~/dev/DRF$ python manage.py shell
Python 3.12.4 | packaged by Anaconda, Inc. | (main, Jun 18 2024, 15:12:24) [GCC 11.2.0]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.27.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from patients.serializers import PatientSerializer

In [2]: PatientSerializer
Out[2]: patients.serializers.PatientSerializer

In [3]: data = {"first_name": "Luis", "last_name": "Martinez"}

In [4]: serializer = PatientSerializer(data=data)

In [5]: serializer
Out[5]: 
PatientSerializer(data={'first_name': 'Luis', 'last_name': 'Martinez'}):
    id = IntegerField(label='ID', read_only=True)
    first_name = CharField(max_length=100)
    last_name = CharField(max_length=100)
    date_of_birth = DateField()
    contact_number = CharField(max_length=15)
    email = EmailField(max_length=254)
    address = CharField(style={'base_template': 'textarea.html'})
    medical_history = CharField(style={'base_template': 'textarea.html'})

In [6]: serializer.is_valid()
Out[6]: False

In [7]: serializer.errors
Out[7]: {'date_of_birth': [ErrorDetail(string='This field is required.', code='required')], 'contact_number': [ErrorDetail(string='This field is required.', code='required')], 'email': [ErrorDetail(string='This field is required.', code='required')], 'address': [ErrorDetail(string='This field is required.', code='required')], 'medical_history': [ErrorDetail(string='This field is required.', code='required')]}

In [8]: exit()