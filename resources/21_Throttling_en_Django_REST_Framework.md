Limitar las solicitudes a una API es fundamental para evitar abusos y proteger los recursos del servidor. El throttling es una técnica clave en este proceso, ya que permite controlar la cantidad de solicitudes que diferentes usuarios pueden hacer en un determinado periodo, previniendo ataques como DDoS y optimizando el rendimiento.


¿Cómo implementar throttling en Django REST?

Para controlar las solicitudes en Django REST, es importante definir reglas específicas. Estas reglas pueden basarse en el estado del usuario, como si está autenticado o es anónimo, o incluso establecer limitaciones distintas para usuarios VIP.

- Primero, debemos entender que el throttling se configura de manera similar a los permisos y autenticación.
- Definimos límites como “requests por minuto”, y estos valores pueden ser diferentes para usuarios anónimos o autenticados.


¿Cómo definir reglas de throttling en Django REST?

La documentación de Django REST proporciona ejemplos claros para limitar las solicitudes de acuerdo al tipo de usuario:

- Para usuarios anónimos: 100 solicitudes por día.
- Para usuarios autenticados: 1000 solicitudes por día.

Estas reglas pueden configurarse fácilmente para ser más estrictas, limitando, por ejemplo, a 5 solicitudes por minuto para usuarios anónimos.


¿Cómo probar la configuración?
1. Modificar la configuración: Añade las reglas de throttling al diccionario de configuración de Django REST. Para limitar a 5 solicitudes por minuto, establece la tasa en 'minute': 5 para usuarios anónimos.
2. Ejecutar el servidor: Después de realizar los cambios, corre el servidor de desarrollo y prueba enviando solicitudes repetidas.
3. Verificación en la terminal: Al alcanzar el límite de solicitudes, Django REST mostrará el error “too many requests” en la terminal, indicando que el sistema de throttling está funcionando correctamente.


¿Qué sucede cuando el límite es alcanzado?

Si un usuario anónimo intenta hacer más de 5 solicitudes en un minuto, verá un error que le informará que ha alcanzado el límite de solicitudes permitidas. Después de esperar unos segundos, el sistema volverá a permitir solicitudes. Este proceso asegura que los recursos del servidor no se saturen con solicitudes abusivas o incorrectas.


Links:

1 - Throttling:
https://www.django-rest-framework.org/api-guide/throttling/