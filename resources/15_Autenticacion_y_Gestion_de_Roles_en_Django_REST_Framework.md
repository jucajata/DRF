En muchos sistemas, las APIs dependen de la autenticación y autorización para proteger recursos sensibles. Este artículo explica ambos conceptos a través de ejemplos y luego los implementa utilizando Django REST Framework.


¿Qué es la autenticación y cómo funciona en las APIs?

La autenticación se refiere a la comprobación de la identidad de un usuario. Imagina que llegas a un hotel, te solicitan tu documento de identificación, y de esta forma, demuestras quién eres. En el mundo digital, es similar: te identificas con un usuario y una contraseña. En Django, esta autenticación genera una cookie que luego es enviada en cada request para identificar y autorizar al usuario.


¿Cómo se implementa la autenticación en Django REST Framework?

Django REST Framework incluye múltiples sistemas de autenticación por defecto. Los más comunes son:

- Session Authentication: Usa cookies y las credenciales del usuario almacenadas en la base de datos de Django.
- Token Authentication: Similar a la llave de un hotel, donde el token identifica al usuario después de autenticarse.

Para implementar el sistema de autenticación en Django, se configuran las clases de autenticación dentro de settings.py, lo cual permite que solo los usuarios autenticados interactúen con los endpoints.


¿Cómo se configura la autorización en Django REST?

La autorización determina qué puede hacer un usuario autenticado. En el ejemplo del hotel, tener la llave te permite acceder solo a tu habitación, pero no a otras. En Django, se define qué usuarios tienen permiso para acceder o modificar ciertos recursos.

Para configurar esto:

1. Se añaden Permission Classes en los viewsets.
2. Se utiliza la clase IsAuthenticated para requerir que el usuario esté logueado antes de realizar cualquier acción.


¿Cómo manejar permisos más avanzados en Django REST Framework?

En algunos casos, es necesario definir permisos personalizados. Por ejemplo, solo los doctores deberían poder modificar ciertos recursos. Para implementar esto, puedes:

- Crear grupos de usuarios, como el grupo “Doctors”.
- Definir clases personalizadas de permisos, como IsDoctor, que verifica si el usuario pertenece al grupo adecuado.

Este sistema permite implementar roles de usuario más complejos, asegurando que solo aquellos con permisos específicos puedan realizar ciertas acciones.


¿Cómo probar la autenticación y autorización en Django?

Después de configurar todo, es importante probar que los permisos y la autenticación funcionan como se espera. Esto incluye:

- Probar con usuarios que tienen acceso y verificar que pueden realizar las acciones permitidas.
- Probar con usuarios sin permisos y asegurarse de que reciban los errores apropiados (como 401 o 403).

Con esta configuración, tus APIs estarán protegidas y listas para manejar autenticación y permisos de manera segura y eficiente.


Links:

1 - How to use sessions | Django documentation | Django
https://docs.djangoproject.com/en/5.1/topics/http/sessions/