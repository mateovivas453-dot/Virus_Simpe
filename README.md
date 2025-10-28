# Virus_Simpe

PROYECTO EDUCACIONAL: RASTREADOR DE TECLADO

Este proyecto ha sido creado estrictamente con fines educativos y de seguridad informática para comprender el funcionamiento de los mecanismos de registro de pulsaciones (keyloggers).

DISCLAIMER IMPORTANTE: El uso de este código para monitorear o acceder a información de terceros sin su consentimiento es ilegal y no ético. La responsabilidad de su uso recae enteramente sobre el usuario.

Dependencias Requeridas

Este script utiliza la librería de Python keyboard. Debe instalarla antes de la ejecución:

pip install keyboard


Uso y Ejecución

Guardar: Guarde el código en un archivo Python (ej., rastreador.py).

Iniciar el Rastreador:
Abra su terminal (o Símbolo del sistema) y ejecute:

python rastreador.py


Estado: El programa indicará que está corriendo en segundo plano (El programa ahora corre en segundo plano...). La función de escucha (keyboard.hook) está activa.

Detención:
Para detener el rastreador, regrese a la terminal y presione CTRL + C.

Ubicación del Archivo de Registro

El código está configurado para guardar todas las pulsaciones en la carpeta de Descargas del usuario:

Nombre del archivo: registro_sistema.txt

Ruta de guardado: La carpeta de Descargas (Downloads) del usuario actual.

La ruta completa será similar a:
C:\Users\SuUsuario\Downloads\registro_sistema.txt

Notas Técnicas del Código

Función Principal: rastreador_teclado() inicia todo el proceso.

Manejo de Teclas: La función en_tecla(evento) usa un diccionario (teclas_especiales) para convertir teclas como enter y tab en representaciones legibles (\n, cuatro espacios).

Filtro: Las teclas modificadoras (shift, ctrl, alt) son ignoradas para mantener el registro limpio y enfocado solo en el contenido escrito.

Bucle de Ejecución: El bloque try/while True: time.sleep(60) mantiene el programa activo en la memoria para que el hook del teclado pueda funcionar continuamente.


git clone https://github.com/mateovivas453-dot/Virus_Simpe.git virus_simple

