Cuando creamos una API, el objetivo principal es que otros sistemas o desarrolladores puedan integrarse con nuestro sistema de manera eficiente. Para lograr esto, una documentación clara y actualizada es fundamental. Herramientas como DRF Spectacular y Swagger nos facilitan esta tarea, automatizando la generación de la documentación y permitiendo que esté siempre sincronizada con nuestro código.


¿Cómo documentar una API automáticamente?
- Django y Django REST Framework (DRF) nos ofrecen la posibilidad de usar una librería llamada DRF Spectacular. Esta herramienta sigue el estándar OpenAPI para generar documentación automática.
- Este estándar permite que cualquier cambio en las vistas o en los endpoints de la API se refleje inmediatamente en la documentación, sin necesidad de modificarla manualmente.


¿Qué es Swagger y cómo usarlo para la documentación de tu API?
- Swagger es una interfaz visual que muestra la documentación generada por DRF Spectacular. Permite a los desarrolladores interactuar directamente con la API, probar los endpoints y revisar los parámetros y respuestas posibles.
- Además, ofrece la opción de descargar un archivo con el esquema OpenAPI que puede ser utilizado por otras herramientas o interfaces.


¿Cómo crear la aplicación de documentación en Django?
1. Crea una nueva aplicación llamada docs desde la terminal.
  - Registra esta aplicación en la lista de Installed Apps en el archivo settings.py.
2. Instala la librería DRF Spectacular ejecutando el comando pip install drf-spectacular.
  - Registra también esta librería en las aplicaciones instaladas.
3. Configura un esquema automático en settings.py asegurándote de que no haya duplicados en la configuración.


¿Cómo agregar las URLs de Swagger y Redoc?
- Dentro del archivo urls.py de la aplicación docs, agrega las URLs correspondientes a Swagger y Redoc.
- No olvides importar correctamente las rutas con path desde django.urls.
- Agrega las URLs de la aplicación docs en el archivo principal de URLs del proyecto para que estén accesibles.


¿Qué diferencia hay entre Swagger y Redoc?
- Swagger ofrece una interfaz donde puedes interactuar con los endpoints y probar las respuestas sin salir del navegador.
- Redoc es otra interfaz que permite navegar entre los endpoints de forma más organizada, con un buscador y una lista de los recursos disponibles. También muestra detalles de las respuestas y errores posibles.


¿Cómo mejorar la documentación de cada endpoint?
- Puedes agregar descripciones a cada uno de los endpoints en las clases de tus vistas, utilizando comentarios en Python.
- Estos comentarios aparecerán automáticamente en la documentación de Swagger o Redoc, facilitando a otros desarrolladores entender el comportamiento de cada recurso.


¿Qué ventajas ofrece el estándar OpenAPI?
- OpenAPI permite que cualquier herramienta que siga este estándar, como Swagger o Redoc, pueda interpretar el esquema de la API y generar documentación visual.
- Es un formato ampliamente utilizado y compatible con distintas interfaces de usuario.


¿Cómo actualizar la documentación al modificar el código?
- La principal ventaja de utilizar DRF Spectacular es que al modificar el código, la documentación se actualiza de forma automática. Esto garantiza que siempre esté sincronizada y evita que tengas que editar la documentación manualmente.


Links:

1 - Home 2024 - OpenAPI Initiative:
https://www.openapis.org/

2 - The Best API Documentation Tool:
https://redocly.com/

3 - drf-spectacular documentation:
https://drf-spectacular.readthedocs.io/en/latest/
