Para instalar Postman en Debian utilizando el archivo comprimido que descargaste (postman-linux-x64.tar.gz), puedes seguir estos pasos:


1. Navega al directorio donde descargaste el archivo:
Abre una terminal y cambia el directorio a donde hayas descargado el archivo. Si está en la carpeta de descargas, puedes hacer:

cd ~/Descargas


2. Extrae el archivo .tar.gz:
Descomprime el archivo utilizando el comando tar:

tar -xzf postman-linux-x64.tar.gz

Esto creará una carpeta llamada Postman en el mismo directorio.


3. Mueve la carpeta a un lugar adecuado:

Es recomendable mover la carpeta Postman a un lugar como /opt, que es donde suelen instalarse aplicaciones de terceros en sistemas Linux.

sudo mv Postman /opt/Postman


4. Crear un enlace simbólico (opcional, pero recomendado):
Para poder ejecutar Postman desde cualquier lugar con un simple comando, crea un enlace simbólico en /usr/bin:

sudo ln -s /opt/Postman/Postman /usr/bin/postman

Ahora puedes ejecutar Postman simplemente escribiendo postman en la terminal.


5. Crear un lanzador en el menú (opcional):
Si quieres tener un icono en el menú de aplicaciones para Postman, puedes crear un archivo de escritorio (.desktop):

Abre tu editor de texto favorito como nano:

sudo nano /usr/share/applications/postman.desktop

Añade el siguiente contenido:

[Desktop Entry]
Name=Postman
Exec=/usr/bin/postman
Icon=/opt/Postman/app/resources/app/assets/icon.png
Type=Application
Categories=Development;

Guarda el archivo y cierra el editor. Ahora deberías ver Postman en tu menú de aplicaciones.


6. Ejecuta Postman:
Ya sea escribiendo postman en la terminal o buscando el icono en el menú de aplicaciones, puedes ejecutar Postman.


7. Actualizaciones (opcional):
Postman se actualiza automáticamente, por lo que no necesitas preocuparte por actualizaciones manuales. Sin embargo, si en el futuro necesitas actualizarlo manualmente, simplemente descarga la nueva versión, repite el proceso y reemplaza los archivos en /opt/Postman.

¡Con esto ya deberías tener Postman instalado y funcionando en Debian!