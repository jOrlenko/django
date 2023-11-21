from django.http import HttpResponse
from django.template import Template, Context


# Cada funcion es una "Vista", esta es nuestra primera vista
def saludar(request): 
    with open ('/media/josue/data_linux/josue/Documentos/Curso_Django/app1/app1/plantillas/index.html', encoding='UTF-8') as index:
        plantilla = Template(index.read())
    
    nombre = 'Josue Orlenko'
    lenguajes = ['HTML', 'Css', 'JavaScript', 'React', 'Python', 'Django']
    contexto = Context({'nombre':nombre, 'lenguaje':lenguajes})
    renderizado = plantilla.render(contexto)
    return HttpResponse(renderizado)

# Una vista con url dinamica, en este caso, edad que tendra en tal año

def edad_futura(request, anio):
    edad = (anio - 2023) + 38
    document = f"<h1>En el año {anio} tendrás {edad} años</h1>"
    return HttpResponse(document)