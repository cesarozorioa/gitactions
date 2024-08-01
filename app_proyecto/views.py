from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import ProyectoDb,TareaDb
#api vistas
from django.core.serializers import serialize
from django.http import HttpResponse

# Create your views here.
def indexHome(request):
    objeto = ProyectoDb.objects.all().order_by('-id')
    return render(request,'index.html',{'objeto':objeto})

def tareasView(request,id):
    proyecto = get_object_or_404(ProyectoDb,id=id)
    return render(request,'tareas.html',{'objeto':proyecto})
    
#api vistas
def listaProyectos(request):
    lista = ProyectoDb.objects.all().order_by('-id')
    return HttpResponse(serialize('json',lista),content_type='text/json') 

def listaProyectosId(request, id):
    proyecto = get_object_or_404(ProyectoDb,id=id)
    return HttpResponse(serialize('json',[proyecto]),content_type='text/json')  

def actualizar_tarea(request, item_id):
    item = get_object_or_404(TareaDb, id=item_id)
    if request.method == 'POST':
        # Actualizamos el dato, por ejemplo incrementando la cantidad
        item.done = True
        item.save()
        return redirect(indexHome)
    return HttpResponse(status=405)