Los Viewsets en Django REST Framework nos ayudan a simplificar la creación de vistas al reutilizar una clase que agrupa el código necesario para manejar diferentes operaciones sobre un recurso, como listar, crear, actualizar y eliminar. Al integrarlos con los routers, evitamos la necesidad de definir cada URL manualmente, ya que el router se encarga de generar todas las rutas de manera automática.


¿Qué son los Viewsets y cómo funcionan?
- Un Viewset es una clase reutilizable que agrupa todas las operaciones que se suelen realizar con una vista (lista, detalle, creación, actualización, eliminación).
- Al usar Viewsets, reducimos la cantidad de clases y URLs que necesitamos escribir, ya que todas las operaciones se manejan desde un solo lugar.
- En lugar de crear múltiples clases, un solo Viewset puede manejar todas las acciones requeridas para un recurso.


¿Cómo se crea un Viewset?
- Importamos ModelViewSet desde rest_framework.viewsets.
- Definimos una clase que hereda de ModelViewSet, como DoctorViewset.
- Asignamos un QuerySet y un Serializer para definir cómo se gestionará la información y cómo será serializada.

from rest_framework import viewsets
from .serializers import DoctorSerializer
from .models import Doctor

class DoctorViewset(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


¿Cómo se registran los Viewsets con los routers?
- Los routers simplifican la creación de URLs, ya que generan las rutas automáticamente al registrar un Viewset.
- Usamos DefaultRouter de Django REST Framework para registrar el Viewset y generar las rutas correspondientes.

from rest_framework.routers import DefaultRouter
from .viewsets import DoctorViewset

router = DefaultRouter()
router.register(r'doctors', DoctorViewset)
urlpatterns = router.urls


¿Cómo se prueban los Viewsets?
- Una vez registrado el Viewset, podemos verificar las URLs generadas ejecutando el servidor y accediendo a la API.
- Las operaciones de creación, actualización y eliminación de un recurso se pueden realizar directamente en las URLs generadas automáticamente.


¿Qué ventajas ofrecen los Viewsets y los routers?
- Evitamos la repetición de código al gestionar varias operaciones con una sola clase.
- Los routers generan automáticamente las rutas necesarias para cada recurso, lo que facilita su uso y mantenimiento.
- Las URLs generadas tienen nombres claros, lo que permite su uso programático dentro del código.