La implementación de endpoints en Django REST Framework nos permite trabajar con recursos como pacientes, tanto para listarlos como para crearlos, mediante los métodos HTTP adecuados. El siguiente paso será extender estas funcionalidades para modificar y eliminar registros.


¿Cómo implementar la creación de pacientes con POST en el mismo endpoint?

Para permitir tanto la creación como la lectura de pacientes en un único endpoint, utilizamos los métodos GET y POST. GET se encarga de listar los pacientes, mientras que POST crea uno nuevo. Para lograr esto:

- Se verifica el método de la solicitud (GET o POST) usando request.method.
- Si es GET, se continúa listando los pacientes.
- Si es POST, se valida la información enviada en el cuerpo de la solicitud a través de un serializador.
- Si los datos son válidos, se utiliza el método save() para guardar el nuevo paciente en la base de datos.


¿Cómo se manejan los errores de validación en POST?

En caso de que los datos enviados no sean válidos, Django REST Framework captura los errores y los formatea en una respuesta JSON. Esto se hace con raise_exception=True en el serializador, lo que devuelve automáticamente una respuesta con los detalles de los errores sin necesidad de un condicional.


¿Cómo retornar una respuesta adecuada al crear un recurso?

Una vez que el paciente es creado correctamente, el servidor responde con un código de estado HTTP 201, indicando que el recurso fue creado. Esto se hace con Response(status=status.HTTP_201_CREATED), asegurando que el cliente reciba la confirmación adecuada.


¿Cómo mostrar el detalle de un paciente con GET?

Para obtener el detalle de un paciente específico, se utiliza el método GET en un endpoint que incluye un parámetro de la URL, generalmente el ID del paciente:

- Se filtra el paciente por ID con get_object_or_404().
- Si el paciente existe, se devuelve su información en formato JSON.
- Si no existe, se responde con un código de estado 404.


¿Cómo manejar la modificación de un paciente con PUT?

El método PUT permite modificar un paciente existente. Utiliza la misma lógica que GET para obtener el paciente, pero en lugar de devolver los datos, actualiza la información recibida:

- Se verifica si el método es PUT.
- Se validan los datos del paciente con un serializador.
- Si los datos son válidos, se guarda la actualización y se responde con un código 200 indicando éxito.