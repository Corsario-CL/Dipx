## Dipx
Programa en python. 
Para el escaneo y identificacion de los dispositivos conectado en la red.

Aquí tienes un listado de las dependencias utilizadas en el código junto con una breve descripción de sus funciones:

#1. Tkinter

    Descripción: Tkinter es la biblioteca estándar de Python para crear interfaces gráficas de usuario (GUI). Proporciona los elementos básicos necesarios para construir una interfaz de usuario, como botones, etiquetas, entradas, y cuadros de texto.

    Funciones Usadas:
        tk.Tk(): Crea una ventana principal para la aplicación.
        tk.Menu(): Crea un menú desplegable en la ventana.
        tk.Label(): Crea una etiqueta para mostrar texto.
        tk.Entry(): Crea un campo de entrada para que el usuario ingrese texto.
        tk.Button(): Crea un botón que puede ser clicado para realizar una acción.
        tk.Text(): Crea un área de texto para mostrar o editar múltiples líneas de texto.
        tk.MessageBox: Muestra cuadros de diálogo para informar al usuario o solicitar confirmación.

#2. Scapy

    Descripción: Scapy es una biblioteca de Python para manipulación de paquetes de red. Permite enviar, recibir, y analizar paquetes de red, lo cual es útil para tareas como el escaneo de red y la detección de dispositivos.

    Funciones Usadas:
        scapy.ARP(): Crea un paquete ARP para solicitar información sobre direcciones IP en la red.
        scapy.Ether(): Crea un paquete Ethernet, que se usa para encapsular el paquete ARP.
        scapy.srp(): Envía paquetes a nivel de enlace de datos y recibe respuestas, útil para el escaneo de red.

#3. IP Address (ipaddress)

    Descripción: El módulo ipaddress de Python proporciona herramientas para trabajar con direcciones IP y redes, incluyendo validación y manipulación de direcciones IP y rangos.

    Funciones Usadas:
        ipaddress.ip_network(): Valida y trabaja con redes IP. Se utiliza para comprobar si una dirección IP o rango es válido.

#4. PrettyTable

    Descripción: PrettyTable es una biblioteca para mostrar datos tabulares en un formato de tabla legible. Es útil para presentar resultados en una tabla formateada.

    Funciones Usadas:
        PrettyTable(): Crea una tabla que puede ser llenada con filas y columnas.
        add_row(): Añade una fila a la tabla.
        __str__(): Devuelve una representación en cadena de la tabla, para ser visualizada como texto.

#5. filedialog

    Descripción: filedialog es un módulo de Tkinter que proporciona cuadros de diálogo para abrir y guardar archivos.

    Funciones Usadas:
        filedialog.asksaveasfilename(): Muestra un cuadro de diálogo para que el usuario seleccione una ubicación y nombre de archivo para guardar un archivo.

Cómo Instalar las Dependencias

Para instalar las dependencias en un entorno de Python, usa los siguientes comandos:

    Tkinter: Normalmente, Tkinter se instala junto con Python. En caso de no estar disponible, puedes instalarlo con:
        Ubuntu/Debian: sudo apt-get install python3-tk
        Fedora: sudo dnf install python3-tkinter
        Arch Linux: sudo pacman -S tk
