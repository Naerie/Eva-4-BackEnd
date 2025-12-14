# Proceso de desarrollo

## 1. Desarrollo
Se implementaron los CRUDS de las entidades que se aprobaron previamente, se reemplazaron los formularios hechos en HTML por los formularios propios de Django, así como los models para la creación de las tablas en la base de datos. 

Se realizó la gestión completa de las entidades: registrar, actualizar, eliminar y su visualización. Según la tabla, se pueden encontrar funcionalidades faltantes que no se creyeron pertinentes para esa entidad en concreto (ej.: suscripciones no se editan ni se eliminan).
Se conectó la base de datos con MySQL, donde se probaron las distintas funcionalidades con éxito. 
Se aplicó cierto nivel de diseño con un archivo CSS complementando el diseño de Bootstrap.

## 2. To-do list
Para organizar el trabajo, se utilizó una lista de tareas (to-do list) en Notion, que permitió planificar y priorizar las funcionalidades desarrolladas. Algunos ítems menores quedaron pendientes, los cuales se pretenden completar en la próxima iteración del proyecto.

https://www.notion.so/ghostpls/backend-2-28b092edb20e8053836cdd8943b25ed6?source=copy_link

## 3. Para el futuro
Mejorar la interfaz tanto en la página principal como en el dashboard de admin/manager.
- Implementar búsquedas en la página principal, ya que será posible por la implementación de las foreign keys que le faltan al proyecto. 
- Validaciones más extensas.
- Diseño.
- Funciones adicionales como:
    -Carrousel de imagenes para las propiedades.
    -Cambiar los placeholders de la pagina principal.
    -Eliminar con checklist en mensajes.
    -Marcar mensajes como leidos.
    -Paginación en pagina principal.