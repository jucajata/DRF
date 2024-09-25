Las pruebas unitarias son esenciales para garantizar que nuestras APIs funcionen correctamente sin tener que gastar demasiados recursos. Django REST Framework facilita este proceso mediante la clase APIClient, que nos permite simular requests y validar los resultados de forma sencilla y eficiente. A continuación, aprenderemos cómo crear pruebas unitarias en un proyecto de Django utilizando esta herramienta.


¿Cómo se configuran las pruebas unitarias en Django REST Framework?

Para comenzar a crear pruebas en Django REST Framework, necesitamos trabajar con el archivo test.py, el cual se genera automáticamente al crear un proyecto. En este archivo, definimos nuestras pruebas heredando de la clase TestCase, que proporciona todas las funcionalidades necesarias para ejecutar tests en Django.

Dentro de la clase de pruebas, usamos el método setUp para preparar datos comunes que reutilizaremos en todas nuestras pruebas, como la creación de un paciente y un doctor. Aquí, empleamos el ORM de Django para manejar los modelos fácilmente.


¿Qué es el cliente API y cómo se usa?

El cliente APIClient es esencial para nuestras pruebas ya que simula requests HTTP, permitiéndonos probar las respuestas de nuestra API sin hacer requests reales. Esto nos ahorra tiempo y recursos. Además, se configura automáticamente para trabajar con datos JSON, simplificando las pruebas.

Importamos el cliente usando:

from rest_framework.test import APIClient

Esto nos permite realizar operaciones como GET, POST, PUT, y más, directamente desde nuestras pruebas. Por ejemplo, para verificar que una lista de “appointments” devuelve un código 200, simplemente escribimos un test que utiliza el cliente para hacer un request GET a la URL de las citas.


¿Cómo validamos los resultados de las pruebas?

Django REST Framework proporciona el módulo status, que nos permite verificar los códigos de respuesta de manera sencilla. En las pruebas, utilizamos el método self.assertEqual() para comparar el código de estado devuelto por la API con el valor esperado:

from rest_framework import status
self.assertEqual(response.status_code, status.HTTP_200_OK)

Esto nos asegura que el código de la API está funcionando correctamente según lo esperado.


¿Cómo se manejan las URLs en las pruebas?

Para obtener las URLs dinámicamente en nuestras pruebas, utilizamos el método reverse() de Django, que permite construir URLs basadas en sus nombres. Esto es especialmente útil cuando trabajamos con URLs que requieren parámetros, como IDs.


¿Cómo solucionamos errores de permisos en nuestras pruebas?

Es común que algunas vistas en Django REST Framework requieran autenticación o permisos especiales. Si nuestras pruebas fallan debido a permisos, podemos ajustar las configuraciones en el viewset, asegurándonos de que las pruebas se realicen bajo las mismas condiciones que los usuarios reales enfrentarían. Por ejemplo, si solo los doctores pueden ver ciertos datos, debemos asegurarnos de que el usuario en la prueba tenga esos permisos.


¿Qué hacer cuando una prueba falla inesperadamente?

Si una prueba falla, es crucial revisar el error devuelto y ajustar el código según sea necesario. A veces, la falla puede deberse a errores en los permisos o configuraciones en los viewsets. Al corregir estos errores y volver a ejecutar la prueba, podemos validar que los ajustes realizados han solucionado el problema.


Links:

1 - Curso de Unit Testing en Python:
https://platzi.com/cursos/unit-testing-python/