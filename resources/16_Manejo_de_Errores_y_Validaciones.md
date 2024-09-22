Validar datos correctamente es clave para asegurar que una aplicación funcione de manera segura y confiable. En este caso, exploramos cómo implementar validaciones personalizadas en serializadores de Django REST Framework para garantizar que los datos cumplan con los requisitos específicos del negocio.


¿Cómo implementamos una validación personalizada en Django REST Framework?

Django ya ofrece validaciones básicas, como verificar que un campo sea un email. Sin embargo, para casos específicos, como asegurarse de que un correo pertenezca a un dominio corporativo, necesitamos crear validaciones personalizadas en el serializador. Esto lo logramos usando el método validate_<nombre_del_campo>. Por ejemplo, para validar que un correo termine en @example.com, implementamos lo siguiente:

- Definimos el método validate_email dentro del serializador.
- Verificamos si el valor del campo contiene el dominio correcto.
- Si es válido, retornamos el valor; si no, levantamos una excepción con un mensaje de error.


¿Cómo manejar errores de validación en casos más complejos?

Para validaciones que dependen de múltiples campos, como validar el número de contacto y el estado de vacaciones de un doctor, usamos el método general validate. Este método permite acceder a todos los campos del serializador en forma de diccionario y aplicar lógica personalizada.
Por ejemplo:

- Validamos que el número de contacto tenga al menos 10 caracteres.
- Si el doctor está de vacaciones (is_on_vacation es True) y el número no es válido, lanzamos una excepción que indica que debe corregirse el número antes de continuar.


¿Qué debemos hacer si hay múltiples validaciones?

En casos donde existen múltiples validaciones, podemos usar un diccionario que devuelva los valores de todos los campos y agregar la lógica en consecuencia. Esto es útil cuando debemos validar múltiples condiciones que se interrelacionan.

¿Cómo lanzamos errores personalizados en serializadores?

Django REST Framework nos permite lanzar excepciones personalizadas que se retornan como un error en formato JSON. Usamos raise serializers.ValidationError para generar estos errores con mensajes específicos, ayudando a los usuarios a corregir los datos enviados antes de que se procesen.


Links:

1 - Serializing Django objects | Django documentation | Django:
https://docs.djangoproject.com/en/stable/topics/serialization/#serializing-data

2 - Exceptions - Django REST framework:
https://www.django-rest-framework.org/api-guide/exceptions/