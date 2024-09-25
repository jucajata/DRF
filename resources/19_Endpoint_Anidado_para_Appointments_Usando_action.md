El endpoint para agendar una cita es esencial dentro de la lógica de negocio, ya que permite la interacción entre pacientes y doctores de manera eficiente. A través de este endpoint, un paciente puede reservar una cita con un doctor, cumpliendo con las mejores prácticas de REST y utilizando un viewset anidado para aprovechar los recursos previamente creados.


¿Cómo se estructura la URL para agendar una cita?

La URL para agendar una cita sigue una estructura anidada basada en el ID del doctor. Utilizamos el recurso existente /doctors/{id} para obtener detalles de un doctor, y sobre esta misma estructura se agregan las citas con el endpoint /appointments. Según REST, un GET en este endpoint devolverá una lista de citas, mientras que un POST permitirá crear una nueva.


¿Cómo se implementa la acción para crear una cita?

Para implementar la acción, es necesario definir un método en el viewset del doctor, que maneje tanto GET como POST. El objetivo principal del POST es recibir los datos de la cita que desea agendar el usuario y crearla utilizando un Serializer. Aquí, el ID del doctor se obtiene de la URL, asegurando que no se pueda modificar desde el formulario.

Pasos clave:

- Se importa el AppointmentSerializer desde el módulo bookings.
- Se recibe la data del request y se agrega el ID del doctor a dicha data.
- Se valida la información a través del método isValid.
- Finalmente, se guarda la cita con Serializer.save() y se retorna un estado 201 (creado).

¿Cómo se filtran las citas de un doctor?

Para retornar las citas de un doctor con un GET, se filtran las citas por el ID del doctor utilizando el ORM de Django. El método filter se encarga de traer todas las citas asociadas al doctor, las cuales se serializan y se devuelven en formato JSON.


¿Cómo se valida la información recibida?

La validación se realiza utilizando el Serializer, el cual se asegura de que los datos cumplan con las reglas establecidas. En caso de que la información no sea válida, se lanza una excepción mostrando un error claro al usuario.


¿Cómo se maneja el estado de las respuestas?

Los estados HTTP se manejan a través del módulo status de Django REST. En el caso de crear una cita, se retorna un estado 201 para indicar que la cita fue creada correctamente. Para las demás acciones, el estado por defecto es 200, indicando que la solicitud fue exitosa.