# Proceso de Desarrollo

## 1. Estructura del Proyecto
El proyecto fue desarrollado en **Django** y organizado en dos aplicaciones principales:

- **main**: destinada al cliente final. Contiene las vistas y templates para el público general (home, contacto, listado de propiedades, suscripciones, etc.).
- **manager**: destinada a la administración. Contiene las vistas, formularios y templates de gestión (propiedades, contactos, visualización de subscripciones, interesados, etc.).

## 2. Flujo de Trabajo
- Se trabajó con **GitHub** como repositorio central.  
- Cada integrante del equipo trabajó en su propia **branch** para desarrollar funcionalidades de manera aislada.  
- Se utilizó el siguiente flujo:
  1. Crear rama a partir de `main`.
  2. Desarrollar la funcionalidad asignada.
  3. Realizar commit y push a la branch.
  4. Fusionar en `main` cuando la funcionalidad een la que se estaba trabajando se completó.

## 3. Desarrollo
- Se definieron los **templates base** (`base-cliente.html` y `base-admin.html`) para mantener una estructura común en cada app.  
- La división en dos apps (`main` y `manager`) permitió un desarrollo más ordenado.  
- En **main** se implementaron páginas como:
  - Home con buscador y carrusel de propiedades.
  - Página de contacto con formulario.
  - Sección “Nosotros” con misión, visión e historia.
  - Suscripción de usuarios a novedades.
- En **manager** se implementaron:
  - Dashboard de administración con accesos rápidos.
  - CRUD de propiedades (registro, listado, eliminación, actualización).
  - CRUD para gestionar tipos de propiedades, disponibilidad y operaciones.
  - Sección de mensajes de contacto recibidos.
  - Visualización de suscripciones e interesados.
  -Simulación de login para el administrador, que redirige al dashboard de gestion.

  Se creo un archivo python para la simulacion de base de datos y poder mostrar ejemplos de propiedades, clientes, tipo de propiedades, estado de propiedades entre otros. 

## 4. Buenas Prácticas
- Uso de **includes** para componentes reutilizables (navbar, sidebar, modals).
- Estilos y componentes basados en **Bootstrap** para garantizar un diseño responsive.
- Separación de lógica de cliente y administrador en distintas apps.
- Uso de **diccionarios/listas** en `datos.py` para simular la base de datos en esta etapa inicial.

## To-do list
Se hizo una lista coperativa de cosas faltantes el dia 9 de septiembre en notion, donde se anotaron las tareas que faltaban realizar hasta el dia 9 de septiembre y los integrantes fueron marcando como completado a medida que se realizaban.
https://www.notion.so/ghostpls/proyectos-templates-263092edb20e8078a3c1cfb9a1b60e66

## Para el futuro
-La realización de validaciones más extensas que solo el tipo de input en los formularios.
-La expancion de las cards de visualización de las propiedades, tanto la vista de los clientes como la de administración.
-Completar las paginas individuales de información de las propiedades en el apartado de clientes.
-Cambiar los placeholders por contenido.
-Utilizar metodologia para el trabajo colaborativo como la lista de to-do de notion.
-Separacion de las paginas individuales de visualizacion de las propiedades.
-implementacion de css para que el proyecto tenga estilo relacionado con la empresa.
