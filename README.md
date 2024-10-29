# Tierra Media

![](img/meme.jpg)

Hecho por Carlos Chacón, Jonatan García y Álvaro Fernández

## Objetivo

Motor de un videojuego de rol en el que dos personajes con armas disputan un combate y dependiendo de la suerte y de la potencia del arma gana uno u otro. 

## FEATURES

- *Diccionario de personajes*: Almacena todos los datos de los personajes en un diccionario. 
- *Agregar personajes al diccionario*: Pide al usuario un nombre de personaje y este se añade al diccionario. Si el personaje no existe salta un error. 
- *Agregar armas a los personajes*: Pide al usuario que le añada un arma a un personaje. Si no existe el arma salta un error. 
- *Mostrar personajes del diccionario*: Muestra los detalles completos de todos los personajes que existen en el diccionario. Si el diccionario está vacío, salta un error. 
- *Mostrar personaje por filtro*: Igual que el anterior pero filtrando por facción o por equipamiento. 
- *Simulación de combates*: Le pasamos por consola dos personajes que se encuentren en el diccionario y estos simulan un combate entre ellos. Cada personaje tiene 300 de vida base y cuando uno llega a 0 termina el combate.
- *Menú interactivo*: Menú que se le muestra constantemente al usuario y dependiendo del número que introduzca por consola el programa realiza una función u otra. Si el usuario ingresa el número 9, el programa finaliza.

## Manejo de errores

Hemos introducido unos cuantos manejos de errores en el código, como por ejemplo si el usuario ingresa una letra en el menú interactivo, el programa caza el ValueError y lo maneja a nuestro antojo. 

## ESTRUCTURA DEL PROYECTO

1. Carpeta features/: Aquí se encuentran los trozos de código separados por funcionalidad.
2. Carpeta main/: Aquí se encuentra la clase main, la cual contiene todo lo necesario para que el proyecto funcione, además del método main el cual es el que se va a ejecutar. 
3. Archivo README.md: Es la documentación oficial del proyecto.
4. Archivo .gitignore: Archivo de configuración donde se almacenan todos los archivos y directorios no rastreados por git.

## Trabajo en equipo

Partes del proyecto que hemos realizado cada uno: 
- Carlos Chacón: Personajes, README.md y manejo de errores
- Álvaro Fernández: Equipamiento y ubicaciones 
- Jonatan García: Sistema de combates, menú, documentación y refactorización

### Desarrolladores del proyecto
1. https://github.com/Carlos5Noob
2. https://github.com/Alvarokstar
3. https://github.com/JonatanGarLun