# Paint Modificado - Proyecto en Python

## Descripción general

Este proyecto consiste en la modificación y mejora del juego Paint utilizando Python y la librería freegames. El objetivo principal fue comprender el funcionamiento del código original, modificar distintas funciones del programa y utilizar herramientas de desarrollo como Git, GitHub y ambientes virtuales en WSL Ubuntu.

El programa permite al usuario dibujar diferentes figuras geométricas en pantalla utilizando el mouse y cambiar tanto colores como grosor de dibujo mediante el teclado. Todas las modificaciones fueron realizadas directamente sobre el archivo original del juego paint.py.

Además de la parte de programación, el proyecto permitió practicar el uso de control de versiones utilizando Git y GitHub, realizando commits, push y actualización del repositorio remoto desde la terminal de Ubuntu en WSL.

---

# Juego original

El juego original pertenece al paquete freegames de Python y fue obtenido mediante el siguiente comando:

freegames copy paint

El archivo original incluía funciones básicas de dibujo, sin embargo algunas funciones se encontraban incompletas y existían varias mejoras posibles tanto visuales como funcionales.

---

# Objetivo del proyecto

El objetivo de este proyecto fue:

- Comprender la estructura básica de un programa en Python.
- Modificar código existente.
- Implementar nuevas funcionalidades.
- Aprender el uso de ambientes virtuales.
- Utilizar Git y GitHub desde la terminal.
- Ejecutar y probar programas gráficos utilizando WSL Ubuntu.

---

# Modificaciones realizadas

Durante el desarrollo del proyecto se realizaron diversas modificaciones al código original del juego Paint.

## 1. Agregado de nuevos colores

Se añadieron nuevos colores disponibles para el usuario, permitiendo una experiencia más completa y personalizada al momento de dibujar.

Los colores agregados fueron:

- Morado
- Naranja
- Rosa
- Café
- Amarillo

Cada color fue asociado a una tecla específica para facilitar su uso durante la ejecución del programa.

---

## 2. Implementación de la función de círculo

Se completó la función encargada de dibujar círculos, la cual originalmente no se encontraba terminada en el código base.

Esta función permite crear círculos utilizando la distancia entre dos puntos seleccionados por el usuario como referencia para el radio.

---

## 3. Implementación de rectángulos

Se agregó una nueva función para dibujar rectángulos, permitiendo ampliar las herramientas geométricas disponibles dentro del juego.

El usuario puede seleccionar la figura y dibujarla directamente sobre la ventana gráfica.

---

## 4. Implementación de triángulos

Se desarrolló una nueva función para dibujar triángulos utilizando coordenadas obtenidas mediante el mouse.

Esta modificación permite generar nuevas formas geométricas dentro del programa.

---

## 5. Cambio dinámico de grosor

Se agregó un sistema para modificar el grosor de las líneas utilizando las flechas del teclado.

- Flecha arriba: aumenta el grosor.
- Flecha abajo: disminuye el grosor.

Esto mejora considerablemente la personalización del dibujo.

---

## 6. Mejoras visuales

Se ocultó el cursor de turtle utilizando la función:

hideturtle()

Esto permite que la ventana gráfica tenga una apariencia más limpia y profesional durante la ejecución.

---

## 7. Organización y documentación del código

El código fue reorganizado y comentado para mejorar la legibilidad y facilitar futuras modificaciones.

También se agregaron nombres de variables más descriptivos y separación lógica entre funciones.

---

# Controles del programa

## Selección de figuras

- l = línea
- s = cuadrado
- c = círculo
- r = rectángulo
- t = triángulo

---

## Selección de colores

- k = negro
- b = azul
- e = rojo
- g = verde
- y = amarillo
- p = morado
- o = naranja
- i = rosa
- n = café

---

## Control de grosor

- Flecha arriba = aumentar grosor
- Flecha abajo = disminuir grosor

---

# Tecnologías utilizadas

Durante el desarrollo del proyecto se utilizaron las siguientes herramientas y tecnologías:

- Python 3
- Turtle Graphics
- Freegames
- Git
- GitHub
- Ubuntu WSL
- Nano Editor

---

# Comandos utilizados

## Activación del ambiente virtual

source ./games/bin/activate

---

## Ejecución del programa

python3 paint.py

---

## Comandos de Git utilizados

git add .

git commit -m "Modificaciones al juego"

git push

---

# Aprendizajes obtenidos

Gracias a este proyecto fue posible comprender mejor el funcionamiento de Python y la modificación de programas ya existentes.

También se aprendió a trabajar utilizando control de versiones con Git y GitHub, así como el uso de ambientes virtuales para mantener organizadas las dependencias del proyecto.

Además, el proyecto ayudó a familiarizarse con el entorno Linux mediante WSL Ubuntu y el uso de comandos desde terminal.

---

# Conclusión

El proyecto permitió modificar exitosamente el juego Paint original añadiendo nuevas funciones, colores y mejoras visuales.

Se logró integrar conocimientos de programación, manejo de terminal, ambientes virtuales y control de versiones, obteniendo un programa funcional y más completo que la versión original.

Finalmente, el proyecto ayudó a desarrollar habilidades importantes relacionadas con desarrollo de software y trabajo colaborativo utilizando herramientas profesionales.

---

# Autor

Ivan Hernandez 
