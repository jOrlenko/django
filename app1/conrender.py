#from django.template.loader import get_template
from django.shortcuts import render

def conrender(request): 
    nombre = 'Nick Salcedo'
    estilos = ['Básico en crema', 'Buttercream', 'Pasta Ballina', 'Estilos Vintage', 'Estilo Cartoon', 'Estilo Realista']
    contexto = {'nombre':nombre, 'decorados':estilos}
    return render(request, 'home.html', contexto)