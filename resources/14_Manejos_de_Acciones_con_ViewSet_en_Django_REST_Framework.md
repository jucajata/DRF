Al crear APIs en Django REST Framework, no solo trabajamos con URLs para recursos, sino también con acciones que permiten ejecutar operaciones específicas, como el pago de una tarjeta o, en este caso, gestionar las vacaciones de un doctor.


¿Cómo agregar un campo para controlar el estado de vacaciones en un modelo?
- En el modelo Doctor, añadimos el campo is_on_vacation, que será un campo booleano con valor predeterminado False.
- Creamos las migraciones con manage.py makemigrations y luego ejecutamos migrate para aplicar los cambios en la base de datos.


¿Cómo crear una acción personalizada para activar o desactivar vacaciones?
- En los ViewSets de Django REST Framework, las acciones personalizadas se crean con el decorador @action. Importamos el decorador desde rest_framework.decorators.
- Definimos un método llamado toggle_vacation con el decorador y especificamos que solo se permitirá el método POST.
- El decorador también necesita el parámetro detail=True para que la acción se aplique a un recurso específico, como un doctor identificado por su ID en la URL.


¿Cómo implementar la lógica para alternar el estado de vacaciones?
- Utilizamos el método get_object() del ViewSet para obtener el objeto Doctor actual.
- La lógica alterna entre el valor True y False para el campo is_on_vacation. Si está en True, lo cambia a False y viceversa.
- Se guarda el objeto Doctor y se retorna una respuesta utilizando Response para informar el estado actualizado.


¿Cómo mejorar la idempotencia y claridad del endpoint?
- En lugar de alternar entre True y False, creamos dos acciones separadas: una para activar vacaciones (set_on_vacation) y otra para desactivarlas (set_off_vacation).
- Esto asegura que cada petición POST tenga un comportamiento predecible, lo que mejora la idempotencia del endpoint.


¿Cómo ajustar la URL de la acción para mejorar la legibilidad?
- Las URLs generadas a partir del nombre del método pueden tener guiones bajos, lo cual no es ideal para SEO y legibilidad. Usamos el parámetro url_path dentro del decorador @action para definir URLs con guiones, por ejemplo, set-on-vacation.


¿Cómo probar las acciones personalizadas?
- Desde la interfaz de Django REST Framework, probamos las acciones enviando peticiones POST a las URLs generadas.
- Verificamos que los doctores puedan ser marcados como en vacaciones o no, y que el campo is_on_vacation cambie correctamente en la base de datos.


¿Cómo replicar este proceso para otros recursos?
- Siguiendo este patrón, podemos crear acciones para otros recursos. Por ejemplo, un paciente puede necesitar obtener un reporte médico en formato JSON, lo cual sería una acción personalizada en el ViewSet de Patient.