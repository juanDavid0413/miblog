from django.shortcuts import render,redirect
from .models import Publicacion
from .forms import PublicacionModelForm
from django.db.models import Q
from django.core.paginator import Paginator


def lista_publicaciones(request):
    query = request.GET.get('q')
    publicacion_list = Publicacion.objects.all()
    fecha_min = request.GET.get('fecha_min')
    fecha_max = request.GET.get('fecha_max')
   
    if fecha_min and fecha_max:
        publicacion_list = publicacion_list.filter(fecha_publicacion_gte=fecha_min, fecha_publicacion_lte=fecha_max)

    if query:
        publicacion_list = publicacion_list.filter(Q(titulo__icontains=query) | Q(contenido__icontains=query))        

    paginator = Paginator(publicacion_list, 10)
    page_number = request.GET.get('page')
    publicaciones = paginator.get_page(page_number)

    return render(request, 'lista_publicaciones.html', {'publicaciones': publicaciones})


def inicio(request):
    return render(request, 'inicio.html')


def agregar_publicacion(request):
    if request.method == 'POST':
        form = PublicacionModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('lista_publicaciones')
    else:
        form = PublicacionModelForm()
    return render(request, 'agregar_publicacion.html', { 'form': form })

def detalle_publicacion(request, pk):
    publicacion = Publicacion.objects.get(pk=pk)
    return render(request, 'detalle_publicacion.html', {'publicacion': publicacion})

def editar_publicacion( request, pk):
    publicacion = Publicacion.objects.get(pk=pk)
    if request.method == 'POST':
        form = PublicacionModelForm(request.POST, instance = publicacion)
        if form.is_valid():
            form.save()
            return redirect('detalle_publicacion', pk=publicacion.pk)
    else:
        form = PublicacionModelForm(instance = publicacion)
        
    return render(request, 'editar_publicacion.html', {'form':form})