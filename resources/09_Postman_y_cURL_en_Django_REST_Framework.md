Para probar de manera eficiente nuestras APIs, es fundamental dominar herramientas especializadas como Postman y Curl. Aunque Django ofrece una interfaz visual para pruebas, el uso de herramientas como estas nos permitirá realizar pruebas más flexibles y personalizadas en diferentes entornos, incluyendo servidores sin interfaz gráfica.


¿Cómo se utiliza Postman para probar una API?

Postman es una herramienta poderosa para interactuar con APIs. Permite realizar requests, gestionar colecciones y simular comportamientos de usuarios. Para probar nuestra API:

- Descarga e instala Postman desde su página principal.
- Accede a la interfaz donde puedes crear nuevos requests.
- Por ejemplo, para listar pacientes en un servidor local, usa la URL: http://localhost:8000/api/patients.
- Selecciona el método GET y presiona Send. Verás la lista de pacientes como respuesta.
- Postman también permite guardar cada request en una colección para su uso posterior, ideal para pruebas repetitivas.


¿Cómo se pueden manejar los requests en la línea de comandos con Curl?

Si no necesitas todas las funcionalidades de Postman o estás en un entorno sin ventanas, Curl es la opción adecuada. Curl te permite ejecutar requests directamente desde la consola, útil cuando estás trabajando en servidores.

- Abre una terminal y utiliza un comando Curl para hacer un request, por ejemplo, listar pacientes con:

curl -X GET http://localhost:8000/api/patients

- También puedes convertir fácilmente un request de Postman a Curl. En la interfaz de Postman, selecciona el ícono de código, copia el comando Curl generado y ejecútalo en la terminal.


¿Cómo crear un paciente nuevo usando Postman?

Para crear un nuevo recurso en nuestra API, como un paciente:

- Selecciona el método POST en Postman.
- Define el cuerpo de la petición en formato JSON, seleccionando Body > Raw > JSON. Por ejemplo:

{
  "name": "Oscar Barajas",
  "age": 30,
  "email": "oscar@example.com"
}

- Ejecuta el request y asegúrate de que la respuesta indique que el recurso fue creado correctamente.
- También puedes generar el comando Curl correspondiente desde Postman y ejecutarlo en la consola.


¿Cómo combinar Postman y Curl para mejorar las pruebas?

Ambas herramientas se complementan bien. Postman facilita la creación y prueba de requests con una interfaz gráfica amigable, mientras que Curl te permite ejecutar esos mismos requests en entornos más limitados. Postman incluso puede generar el código Curl de un request, lo que es muy útil para integrar estos comandos en scripts automatizados o suites de pruebas.


Links:

1 - Postman API Platform:
https://www.postman.com/

2 - curl - Documentation Overview:
https://curl.se/docs/