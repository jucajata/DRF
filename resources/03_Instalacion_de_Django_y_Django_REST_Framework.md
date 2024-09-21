Django REST Framework es una herramienta poderosa para crear APIs de manera rápida, sencilla y escalable. Aprovecha todas las funcionalidades de Django, como los modelos y el sistema de seguridad, y las adapta para crear APIs REST eficaces. Con una configuración adecuada, podemos integrar el framework en nuestros proyectos y empezar a desarrollar de inmediato.


¿Cómo instalar y configurar Django REST Framework?
- Primero, necesitas tener instalado Python. Confirma la instalación con el comando: python3 --version.
- Crea un entorno virtual con: python3 -m venv venv, y actívalo con source venv/bin/activate (Linux/Mac) o consulta los recursos para hacerlo en Windows.
- Instala Django y Django REST Framework con: pip install django djangorestframework.


¿Cómo iniciar un proyecto con Django?
- Crea un nuevo proyecto usando el comando: django-admin startproject doctor_app ..
- Esto generará los archivos necesarios dentro de la carpeta donde estés trabajando.
- Agrega las librerías instaladas a un archivo requirements.txt con el comando: pip freeze > requirements.txt, lo cual es crucial para mantener control sobre las versiones que estás utilizando en tu proyecto.


¿Cómo integrar Django REST Framework en el proyecto?
- Dentro del archivo settings.py, busca la configuración INSTALLED_APPS y agrega 'rest_framework'.
- La documentación oficial de Django REST Framework proporciona detalles sobre su instalación y configuración, lo cual es una excelente fuente de referencia.


¿Qué extensiones son recomendables para mejorar el entorno de desarrollo?
- Usa extensiones como “Python” y “Black” de Microsoft en tu editor para mejorar la experiencia de desarrollo.
  -La extensión de Python te permite realizar depuraciones fácilmente.
  -Black formatea tu código automáticamente conforme al estándar PEP8, ayudando a mantener un código limpio y consistente.


¿Cómo ejecutar el proyecto?
- Ejecuta el servidor de desarrollo con: python manage.py runserver. Esto te permite ver los cambios que realices en tiempo real.
- Visita la URL generada para confirmar que Django se ha configurado correctamente.


Links:
1 - Home - Django REST framework:
https://www.django-rest-framework.org/