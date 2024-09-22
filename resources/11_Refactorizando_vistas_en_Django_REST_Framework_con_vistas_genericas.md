Hemos visto cómo utilizar vistas genéricas en Django para crear vistas de detalle, simplificando el código y evitando la duplicación. A través de la clase RetrieveUpdateDestroyAPIView, podemos obtener, modificar o eliminar recursos de manera eficiente, reduciendo la cantidad de código a manejar.


¿Cómo evitar la duplicación de código con vistas genéricas?
- Django permite usar vistas genéricas como RetrieveAPIView, UpdateAPIView y DestroyAPIView.
- Sin embargo, es más eficiente usar la clase combinada RetrieveUpdateDestroyAPIView, que integra estas tres funcionalidades.
- Con esta clase podemos obtener, actualizar o eliminar un recurso sin necesidad de importar múltiples vistas.


¿Cómo funciona el refactor a las vistas genéricas?
- El código que antes obtenía el objeto y devolvía un error 404 si no se encontraba, ahora es reemplazado por una vista genérica que maneja esa lógica automáticamente.
- Al definir la vista genérica RetrieveUpdateDestroyAPIView, simplemente necesitamos definir las variables correspondientes, como el modelo y los permisos, y se manejan todas las operaciones CRUD (create, read, update, delete).
- Esto nos permite reducir significativamente el código y mantener la funcionalidad.


¿Cómo realizar validaciones con las vistas genéricas?
- Django continúa manejando validaciones, como las que se generan al enviar datos incorrectos, por ejemplo, una fecha inválida.
- Estas validaciones son útiles en formularios de frontend, ya que permiten mostrar al usuario por qué una solicitud ha fallado.


¿Qué sigue después de implementar vistas genéricas?
- El siguiente paso es usar view sets, que nos permitirán agrupar las vistas de una manera más eficiente y evitar la repetición de código.
- Aunque se ha logrado simplificar el código con las vistas genéricas, los view sets llevarán esta simplificación un paso más allá, agrupando operaciones similares en un solo conjunto.


Links:

1 - Viewsets - Django REST framework:
https://www.django-rest-framework.org/api-guide/viewsets/

2 - Generic views - Django REST framework:
https://www.django-rest-framework.org/api-guide/generic-views/