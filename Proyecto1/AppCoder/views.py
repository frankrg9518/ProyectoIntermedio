from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from AppCoder.forms import CursoFormulario

from AppCoder.models import Curso       


def inicio (request):
    return render(request, "AppCoder/inicio.html")

def cursos(request):
    return render(request, "AppCoder/cursos.html")

def profesores(request):
    return render(request, "AppCoder/profesores.html")

def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")
    
def entregables(request):
    return render(request, "AppCoder/entregables.html")

def procesar_formulario(request):
    if request.method != "POST":
        return render(request, "AppCoder/formulario.html")
    curso = Curso(nombre=request.POST["curso"], camada=request.POST["camada"])   
    curso.save()
    return render(request, "AppCoder/inicio.html")

def procesar_formulario2(request):
    if request.method != "POST":
        mi_formulario = CursoFormulario()
    else:
        mi_formulario = CursoFormulario(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
            curso.save()
            return render(request, "AppCoder/inicio.html")
    contexto = {"formulario":mi_formulario} 
    return render(request, "AppCoder/formulario.html",contexto)

def busqueda(request):
    return render(request, "AppCoder/busqueda.html") 

def busqueda_2(request):
    return render(request, "AppCoder/busqueda_2.html")

def buscar(request):
    respuesta = f"Estoy buscando la camada nro: {request.GET['camada']}"    
    return HttpResponse(respuesta)


def buscar_2(request):
    if not request.GET["camada"]:
        return HttpResponse("Datos no enviados")
    else:
        camada_buscar = request.GET["camada"]
        cursos_encontrados = Curso.objects.filter(camada=camada_buscar)

        contexto = {"camada": camada_buscar, "cursos": cursos_encontrados} 

        return render(request, "AppCoder/resultado_busqueda.html", contexto) 



