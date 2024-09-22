Refactorizar nuestras vistas basadas en funciones a vistas basadas en clases no solo mejora la organización del código, sino que también lo hace más escalable y reutilizable. En esta clase, hemos visto cómo Django REST Framework nos facilita aún más esta tarea al proporcionar vistas genéricas que reducen considerablemente la cantidad de código que tenemos que escribir manualmente.


¿Cómo refactorizar una vista basada en funciones a una basada en clases?
- Comenzamos importando APIView desde Django REST Framework.
- Creamos una nueva clase, heredando de APIView, donde definimos los métodos como get, post, o delete.
- Esto nos permite organizar mejor el código y evitar los condicionales que usamos en las vistas basadas en funciones.


¿Cómo conectar la vista basada en clases con una URL?
- Debemos importar la nueva vista en el archivo de URLs y reemplazar la vista basada en función por la basada en clase.
- Recordemos usar el método as_view() al conectarla en el archivo de URLs.


¿Qué beneficios ofrecen las vistas genéricas en Django REST?

Las vistas genéricas permiten simplificar aún más el código, reutilizando funcionalidad ya existente en Django REST:

- Usamos ListAPIView para simplificar una vista que solo lista elementos.
- Usamos CreateAPIView para manejar la creación de recursos.
- Podemos heredar de varias vistas genéricas a la vez para combinar funcionalidades, como listar y crear con pocas líneas de código.


¿Cómo funciona el QuerySet y el SerializerClass en las vistas genéricas?
- Definimos un QuerySet para obtener los datos que queremos listar o manipular.
- Asociamos una clase de serialización con SerializerClass para transformar los datos según las necesidades de nuestra API.
- Esto nos permite eliminar métodos como get o post, ya que se gestionan automáticamente.


¿Cómo evitar duplicar código?

Uno de los principales objetivos al usar clases es evitar la duplicación de código. Con vistas genéricas podemos reutilizar los mismos parámetros y métodos que ya vienen implementados, logrando que el código sea más limpio y fácil de mantener.


Links:

1 - Django REST Framework 3.14 -- Classy DRF
https://www.cdrf.co/