# Proyecto EDDYPOO-REY

# Sistema de Gestión Académica (SGA)

El Sistema de Gestión Académica (SGA) es un proyecto de software diseñado para administrar y automatizar diversas funciones relacionadas con la gestión académica en una institución educativa. El objetivo principal del proyecto es facilitar la organización y seguimiento de las actividades académicas, tanto para alumnos como para profesores y administrativos.

## Características principales y funcionalidades

- **Registro y gestión de usuarios:** El sistema permite registrar y gestionar usuarios, incluyendo alumnos, profesores y administrativos. Cada usuario cuenta con información personal, como nombre, apellido, DNI, fecha de nacimiento, sexo, entre otros datos relevantes.

- **Gestión de materias y carreras:** El SGA permite administrar un catálogo de materias y carreras ofrecidas por la institución. Los usuarios pueden inscribirse en materias, visualizar las materias activas y aprobadas, y actualizar su historial académico.

- **Calificaciones y notas:** El sistema facilita la carga y actualización de calificaciones y notas por parte de los profesores. Los alumnos pueden consultar sus notas y saber si han aprobado o no una materia.

- **Trámites y solicitudes:** Los usuarios pueden iniciar trámites y solicitudes relacionados con la administración académica. Estos trámites son gestionados por el personal administrativo asignado, lo que permite un seguimiento eficiente y una resolución oportuna.

## Tecnologías utilizadas

El proyecto del Sistema de Gestión Académica se desarrolla utilizando las siguientes tecnologías:

- Lenguaje de programación: `Python`
- Interfaz de usuario: `PyQt5`
- Base de datos: `Pickle`
- Librerias externas: `MatPlotlib`, `Qt-material`, `PyQt5-tools`

_Observación:_ Todas las librerias se pueden instalar con `pip install`

## Testing

**Run Code**

Como hay dos versiones (_ver las aclaraciones_), se crearon dos archivos `main.py`. Uno se encuentra dentro de la carpeta Proyecto y el otro dentro de la carpeta repositorio (EDDYPOO-REY_V2.0). Desde estos dos archivos se debe correr el programa.
- Para correr la versión 1: `main.py` que se encuentra dentro de la carpeta Proyecto
- Para correr la versión 2: `main.py` que se encuentra dentro de la carpeta del repositorio

**Usuarios** 

- Administrativo: el legajo es AD10000 y su contraseña 41741232
- Alumnos: hay varios creados para testing, un ejemplo para ingresar seria con el legajo 62523 y la contraseña 43046873
- Profesor: el legajo es PR10000 y su contraseña 23123141

_Observación:_ Hay algunos objetos creados para testing que no poseen todos sus atributos completos, esto se debe que fueron utilizados para otro propósito (los objetos usuarios expresados arriba, sí los poseen).

## Aclaraciones

- La carpeta ProyectoV2 se creó especificamente para poder importar las clases de la versión anterior (solo se hacen modificaciones en los `import`). Lo hicimos de esta manera para tener disponible la versión anterior que tiene todas las funcionalidades y validaciones correspondientes (código que se encuentra en la carpeta Proyecto).

- Se desarrolló una interfaz de usuario (GUI) completa y funcional, pero no se pudo integrar todo el codigo realizado en la versión anterior. Es decir, la versión 1 que tiene el UX/UI en la terminal de Python, posee funcionalidades en términos de validaciones y lógica de programación que todavía no se pudieron implementar en la GUI. Gran parte se llegó a implementar correctamente, de todas formas nos parecía pertinente aclararlo.

## Autores

Este proyecto es desarrollado por Leonel Scalise, Matias Diaz Canton, Federico Nieddu, Tomas Elffman, Martin Pimentel como parte practica de Estructura de Datos y Programacion.

---
 
