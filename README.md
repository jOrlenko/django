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
Una vez que migró el manage.py debemos iniciar una base de datos, que es requisito para el funcionamiento de Django. Por defecto, Django, viene con `Qlite3` y debemos inicializarlo.

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

## Bucles 
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