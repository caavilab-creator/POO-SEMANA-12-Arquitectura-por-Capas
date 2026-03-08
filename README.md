# 📚 Sistema de Gestión de Biblioteca Digital

Proyecto desarrollado para la **Semana 12 - Programación Orientada a Objetos**, aplicando arquitectura por capas y principios de diseño de software.

## 📋 Descripción

Sistema de gestión de biblioteca digital que permite administrar libros, usuarios y préstamos. Implementa una arquitectura estructurada por capas (modelos, servicios y punto de entrada), separando correctamente la lógica del negocio de la ejecución del programa.

## 🎯 Objetivos

- Aplicar correctamente la Programación Orientada a Objetos
- Implementar una arquitectura por capas bien estructurada
- Separar responsabilidades entre modelos, servicios y punto de entrada
- Utilizar estructuras de datos apropiadas (tuplas, listas, diccionarios, sets)
- Implementar encapsulamiento y buenas prácticas de código

## 🏗️ Estructura del Proyecto

biblioteca_app/

├── modelos/

│ ├── init.py

│ ├── libro.py # Entidad Libro

│ └── usuario.py # Entidad Usuario

├── servicios/

│ ├── init.py

│ └── biblioteca_servicio.py # Lógica de negocio

└── main.py # Punto de entrada y menú interactivo

## 🚀 Funcionalidades

### Gestión de Libros

- ✅ Añadir libros al catálogo
- ✅ Quitar libros del sistema
- ✅ Buscar libros por título, autor o categoría

### Gestión de Usuarios

- ✅ Registrar nuevos usuarios
- ✅ Dar de baja usuarios

### Préstamos y Devoluciones

- ✅ Prestar libros a usuarios
- ✅ Devolver libros prestados
- ✅ Listar libros prestados por usuario

  💻 Ejemplo de Uso

==================================================
📚 SISTEMA DE GESTIÓN DE BIBLIOTECA DIGITAL
==================================================

1. Añadir libro
2. Quitar libro
3. Registrar usuario
4. Dar de baja usuario
5. Prestar libro
6. Devolver libro
7. Buscar libros
8. Listar libros prestados a usuario
9. Mostrar todos los libros
10. Mostrar todos los usuarios
0. Salir
   
==================================================

Seleccione una opción: 




