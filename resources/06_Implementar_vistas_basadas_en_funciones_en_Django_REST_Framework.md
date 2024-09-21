Cómo crear una vista basada en funciones que nos permita listar los pacientes en nuestra base de datos utilizando Django REST Framework y serializadores. Además, configuraremos las rutas y endpoints para consumir esta funcionalidad desde el frontend o cualquier cliente que utilice el API.


¿Cómo creamos una vista para listar pacientes utilizando serializadores?

Primero, abrimos nuestro archivo de vistas y realizamos las siguientes importaciones necesarias:

- Importamos el PatientSerializer desde los serializadores.
- Traemos el modelo Patient desde el archivo de Modelos.
- Importamos la clase Response desde Django REST Framework, que nos permitirá devolver datos en formato JSON o XML, entre otros.

Luego, creamos una función llamada ListPatients que será nuestra vista basada en funciones. Esta función hará una consulta a la base de datos para obtener todos los pacientes. Para esto, usamos Patient.objects.all() y guardamos el resultado en una variable.


¿Cómo usamos el serializador para manejar la lista de pacientes?

Una vez que obtenemos los pacientes, necesitamos serializar los datos. Para ello, usamos el PatientSerializer, pero como estamos serializando una lista de objetos, pasamos el parámetro many=True. Esto le indica al serializador que procese múltiples ítems.

La data serializada estará disponible en serializer.data, que será lo que devolvemos en el Response.


¿Cómo agregamos un decorador a nuestra vista?

Para que Django REST Framework reconozca nuestra vista, necesitamos usar el decorador @api_view. Lo importamos desde rest_framework.decorators. Este decorador se configura para que la vista solo acepte peticiones GET. De esta manera, evitamos que se utilicen otros métodos HTTP, como POST, en esta misma URL.


¿Cómo configuramos la URL para la vista?

Abrimos el archivo de configuración de URLs y creamos una nueva ruta. Asociamos el path api-patients con la vista ListPatients, importándola desde el archivo de vistas.

Guardamos todo y ejecutamos el servidor con el comando manage.py runserver.


¿Qué muestra el API cuando accedemos al endpoint?

Al acceder a la URL api-patients, Django REST Framework nos muestra un listado de pacientes en formato JSON. Este listado incluye toda la información de los pacientes almacenados en la base de datos, con campos como nombres, apellidos y fechas. Las fechas aparecen en formato de cadena, aunque en el modelo de Python están como DateTime.


¿Qué reto sigue después de listar pacientes?

El siguiente paso es crear un nuevo endpoint que permita añadir pacientes a través del método POST. El reto será validar que los datos enviados coincidan con las reglas definidas en el modelo, usando nuevamente los serializadores.