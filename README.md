# Proyecto:  Books & Tea

## Primer Entrega Proyecto Final - Coderhouse

### Acerca
La idea de este proyecto es el primer paso previo a la entrega final, que será 
un blog respecto a libros y comidas que podemos relacionar, ya sea a la historia,
región donde transcurre o autor. 

### Funcionamiento  
En el archivo `requirements.txt` se listan los requerimientos para el 
funcionamiento del proyecto.  
En el archivo `.env` se aloja la `SECRET_KEY` de Django.  

### Descripción
La barra de navegación contiene 5 secciones que se detallan a continuación:

| SECCIÓN | DESCRIPCIÓN |
| -- | -- |
| INICIO | Página de bienvenida.  Aquí funcionará el botón de registro de usuarios.  
| LIBROS | Nos lleva al formulario para cargar los libros que se almacenarán en la base de datos. El formulario solicita: Título, Autor,  ISBN. Este último solicita el ingreso de números (hasta 13 dígitos), sin guiones.  |
| RECETAS | Lleva al formulario para cargar recetas, donde se solicita: Nombre, Preparación. |
| BLOG | Lleva al formulario de carga de posteos para el blog. Este formulario solicita: Título, Subtítulo, Autor, Contenido, Fecha (con formato AAAA-MM-DD)  |
| BUSCAR LIBROS | Esta sección permite buscar libros en la base de datos, con la opción de hacerlo por palabra que se encuentre en el título o por autor.  Abajo de estos formularios, aparecen los resultados de la búsqueda y si no los hubiera, envía un mensaje.  

Se provee una pequeña base de datos para poder comprobar los formularios de búsqueda.  

Autores ingresados (para comprobar la búsqueda por autor):  
- J. K. Rowling
- Mark Twain
- Emily Bronte
- Charlotte Bronte  

Libros ingresados (para buscar por nombre):  
- Harry Potter y el cáliz de fuego
- Harry Potter y las reliquias de la muerte
- Harry Potter y la cámara secreta
- Cumbres borrascosas
- Jane Eyre
- Las aventuras de Tom Sawyer
- Las aventuras de Huckleberry Finn

