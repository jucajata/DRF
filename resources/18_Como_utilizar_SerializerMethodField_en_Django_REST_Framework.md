A veces necesitamos calcular y mostrar valores derivados en el resultado de un endpoint sin alterar el modelo de datos original. Un ejemplo común es calcular la edad de un paciente a partir de su fecha de nacimiento. Para ello, podemos utilizar el SerializerMethodField en Django REST Framework. Este campo permite realizar cálculos utilizando los datos del modelo, como veremos a continuación.


¿Cómo calculamos un valor con SerializerMethodField?

Para calcular un valor, primero debemos definir un nuevo campo en nuestro serializador usando SerializerMethodField. Este tipo de campo permite definir un método que realizará el cálculo y retornará el valor deseado. Aquí te mostramos cómo hacerlo:

- Importa SerializerMethodField desde el módulo serializers.
- Define un nuevo campo en el serializador, por ejemplo, “Age” para calcular la edad.
- Si no especificas un método con el argumento method_name, Django REST Framework generará un nombre por defecto en la forma get_.


¿Cómo calculamos la edad usando la fecha de nacimiento?

La clave del cálculo es restar la fecha de nacimiento del paciente a la fecha actual. Este proceso genera un objeto timedelta, que representa la diferencia en días. Para convertirlo a años, sigue estos pasos:

1. Importa date desde el módulo datetime, que es suficiente ya que trabajamos con fechas (no datetime).
2. Obtén la fecha actual utilizando date.today().
3. Calcula la diferencia entre la fecha actual y la fecha de nacimiento.
4. Divide esta diferencia en días por 365 para obtener la edad aproximada en años.
5. Retorna el valor numérico o, si es necesario, formatea el resultado como un string.

Ejemplo de código:

from rest_framework import serializers
from datetime import date

class PatientSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()

    def get_age(self, obj):
        today = date.today()
        age_timedelta = today - obj.date_of_birth
        age = age_timedelta.days // 365  # Convertimos días a años
        return age

    class Meta:
        model = Patient
        fields = ['name', 'date_of_birth', 'age']


¿Qué sucede si obtenemos resultados incorrectos?

Un problema común al calcular la edad es no acceder correctamente al atributo days del objeto timedelta. Si simplemente restamos las fechas, obtendremos un objeto timedelta, que necesitamos dividir por 365 para convertirlo en años.

Otro detalle importante es no incluir texto como “años” en el resultado, ya que es preferible dejar el formato de presentación (e.g., el idioma) en manos del frontend.


¿Cómo calculamos la experiencia de un doctor?

Siguiendo el mismo patrón que para calcular la edad, podemos calcular la experiencia de un doctor usando su fecha de inicio de trabajo. Solo es necesario reemplazar la fecha de nacimiento con la fecha de inicio laboral.

Ejemplo de código para la experiencia:

class DoctorSerializer(serializers.ModelSerializer):
    experience = serializers.SerializerMethodField()

    def get_experience(self, obj):
        today = date.today()
        experience_timedelta = today - obj.start_date
        experience = experience_timedelta.days // 365
        return experience

    class Meta:
        model = Doctor
        fields = ['name', 'start_date', 'experience']


¿Qué otras aplicaciones tiene el SerializerMethodField?
- Calcular otros valores derivados sin alterar el modelo de datos.
- Agregar lógica personalizada en el serializador sin tocar la base de datos.
- Permitir mostrar valores preprocesados para el frontend sin requerir cambios en el backend.


Links:

1 - datetime - Basic date and time types - Python 3.12.6 documentation:
https://docs.python.org/3/library/datetime.html