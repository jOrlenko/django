# DJANGO

## 01 - Creando un nuevo proyecto
Creamos un nuevo proyecto ejecutando en consola:
```
 django-admin startproyect 'miProyecto'
```

### Configuraciones Iniciales
Primeramente es necesario inicializar el documento `manage.py` que se encuentra en el directorio raiz de nuestro proyecto:
```
python3 manage.py migrate
```
Una vez que migró el manage.py debemos iniciar una base de datos, que es requisito para el funcionamiento de Django. Por defecto, Django, viene con `SQlite3` y debemos inicializarlo.

Para poder visualizar nuestro proyecto inicializando un servidor privado ejecutamos:
```
python3 manage.py runserver
```
### Editor de código
A partir de este punto, trabajaremos directamente desde el editor de código con nuestra App.
## 02 - URL y Views

## 03 - Plantilla
La plantilla es el documento, y contexto, en el que se renderizará nuestro codigo (lógica interna). 
Por un sentido de practicidad, este documento `html` será independiente y se trabajará por separado, permitiendo así que el diseño no esté incrustado en la lógica del programa, y viceversa.

### Creación de la Plantilla
En el documento de Python donde tendremos las vistas necesitamos importar *Template* y *Context* de Django
```
from django.template import Template, Context
```
Hecho esto, ya podemos importar importar en la vista el documento HTML con el que estaremos trajando.
Para ello, podemos crear un documento HTML (recomendado: en una carpeta llamada plantillas), y en el HTML daremos la estructura a nuestro documento como el usuario lo verá. 

Ahora debemos importar ese documento a nuestra vista con Python (por ahora usando `with open()`).

Una vez que nuestra vista tiene el documento, necesitamos crear dos variables impresindibles:

1 - Template: almacena el documento sobre el cual estamos trabajando

2 - Context: en el contecto podemos pasar las variables a renderizar en el template.
Es importante recordar que *siempre* recibirá un dict como parámetro. El cual contiene el formato 'clave':valor
clave: será el nombre que en el doc HTML recibirá la asignacion del valor

En el doc HTML pondremos la clave que ingresa por context entre *doble* llave `{{clave}}`

Ahora unimos todo utlizando `template.render(context)`

Para poder mostrar sólo alguna propiedad de esa clase u objeto, podemos hacerlo: `{{clave.propiedad}}`

### metodos y propiedades en plantilla
Django al encontrarse con `elemento.algo` en una *plantilla* busca la funcion de "algo" con la siguiente jerarquía:
- Diccionario -> comprueba si se trata de un dict, si no lo es, revisa el siguiente
- Atributo -> y así sucesivamente hasta encontrarlo
- Método
- Lista

Es por esto que en django, un método nunca irá con (), y metodos y atributos, etc todas se escriben igual.

## 04 - Bucles 
Debemos recordar que el funcionamiento de aperturas y cierres funciona igual que los tags de html. Por lo cual, si anidamos bucles, el cierre del primero debe estar despues del cierre del primero

### For
Supongamos que debemos enviar una lista, y queremos que esta se renderice independientemente de la cantidad de datos que contenga, en este caso, debemos:
1- pasarla en el dict del render con su clave:valor
2- el bucle for lo escribimos en la plantilla html:
```
<div>
    {% for dato in lista %}
        <p>{{dato}}</p>
    {% endfor%}
</div>
```
### If
Funciona igual que el for. Permite la colocación de else.
```
<div>
    {% if dato %}
        <p>{{dato}}</p>
    {% else %}
        <p>No existe el dato</p>
    {% endif %}
</div>
```

## 05 - Filtros
Podemos aplicar filtros. Incluso concatenarlos.
Se aplican con "|" en la estructura de la platilla
```
nombre|first
```
Este filtro, por ejemplo, hace que solo se renderice la primer letra de la cadena nombre
```
nombre|first|lower
```
Ahora le estamos pidiendo que, ademas, lo ponga en minúscula
Más info en <a href='https://django-filter.readthedocs.io/en/stable/' target=_blank>Documentacion oficial</a>

## 06 - Cargadores de Plantillas - Loader
Importante! 
¿¿Porque usar *loader* si con open() funciona?? 
Es simple, al usar open estamos sobrecargando el codigo, y haciendo que la app deba realizar muchas más operaciones de las que debería. Por lo tanto, la mejor forma de hacerlo es a través de un loader.

### Configuración
Debemos ingresar en el archivo `setting.py` y buscamos la parte de `TEMPLATES`. 
Dentro veremos que `DIRS` tiene una lista vacía. Aquí debemos poner la ruta de acceso de la carpeta de los templates o plantillas. No se coloca un template directamente, porque el loader debe luego buscarlo.

### Loader
Una vez configurado, entramos en nuestra view e importamos el loader de `django.template`. 
Ahora es muy simple, en una variable, asignaremos el template con `get_template` pasándolo como parámetro. 
```
from django.template import loader
template = loader.get_template('index.html')

from django.template.loader import get_template
template = get_template('index.html')
```
De esta forma, el template se carga en un modo en el que Django comprende con mayor facilidad, por lo cual, ahora el context no es necesario. Y en su lugar sólo nos pide que le pasemos un diccionario. Esto es así porque si bien ambos son clase Template, son clases distintas para Django, por lo que el render funcionará diferente.
```
contexto = {'nombre':nombre, 'lenguaje':lenguajes}
```
**NO DEBEMOS USAR:**
```
contexto = context({'nombre':nombre, 'lenguaje':lenguajes})
```

## 07 - Render (shortcuts)
Podemos importar:
```
from django.shortcuts import render
```
Este render nos permite hacer un renderizado más limpio.
Requiere de dos parámetros obligatorios: request y template (que se lo pasamos directamente con el nombre del archivo html entre comillas); pero opcionalmente podemos asignarle un context como tercer parámetro pasándole directamente el diccionario
```
def laVista(request):
    diccionario = {'clave':'valor'}
    return render(request, 'index.html', diccionario)
```

## 08 - Plantillas Anidadas
Normalmente, nuestra pagina web requerira de varios documentos web que la componen, tal como la barra de navegación, que se muestra en todo el sitio, etc.

En el template index.html (o el que renderizará el template anidado), debemos llamar al template de la siguiente forma:
```
{% include 'anidado.html' %}
```
### Herencia de plantillas
No es rentable estar anidando plantillas. Para el caso de necesitar una plantilla pero de contenido cambiante, es mejor tener una plantilla padre de la que se heredará como en las clases de Python.
Se coloca en cada plantilla hija como primer etiqueta.
```
{% extends 'plantillaPadre.html' %}
```

## 09 - Bases de Datos
Por defecto, Django trabaja con SQLite3, por lo cual es muy facil trabajarlo. Pero eso no implica que no se puedan manejar otras bases de datos.

#### Diferencia en Django entre 'Proyecto' y 'Aplicacion'
Un Proyecto es con lo que estamos trabajando ahora. Una aplicacion está contenida en un proyecto.
Es posible que, de acuerdo al proyecto, pueda tener más de una aplicacion o ninguna.

**Una aplicacion es como un paquete o módulo que hace una tarea concreta.** o una suma de tareas concretas.
Cuantas apps necesitaré? 1, 4, 8? Depende de la complejidad del proyecto y las funcionalidades que necesitemos

La gran ventaja es la modularizacion, y por ende, la reutilizacion de las apps de un proyecto a otro.

### Cómo se crea una Base de Datos SQLite3?
Django la crea automaticamente, usando la clase Model