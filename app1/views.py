from django.http import HttpResponse
from django.template.loader import get_template

# Cada funcion es una "Vista", esta es nuestra primera vista
def saludar(request): 
    #with open ('/media/josue/data_linux/josue/Documentos/Curso_Django/app1/app1/plantillas/index.html', encoding='UTF-8') as index:
    #    plantilla = Template(index.read())
    plantilla = get_template('index.html')
    
    nombre = 'Nick Salcedo'
    lenguajes = ['Básico en crema', 'Buttercream', 'Pasta Ballina', 'Estilos Vintage', 'Estilo Cartoon', 'Estilo Realista']
    contexto = {'nombre':nombre, 'decorados':estilos}
    renderizado = plantilla.render(contexto)
    return HttpResponse(renderizado)
def edad_futura(request):
    pass