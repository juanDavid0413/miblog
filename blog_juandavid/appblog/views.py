from django.shortcuts import render,redirect
from .models import Publicacion
from .forms import PublicacionModelForm
from django.db.models import Q
from django.core.paginator import Paginator


def lista_publicaciones(request):
    query = request.GET.get('q')
    publicacion_list = Publicacion.objects.all()
    paginator = Paginator(publicacion_list, 10)
    fecha_min = request.GET.get('fecha_min')
    fecha_max = request.GET.get('fecha_max')
    page_number = request.GET.get('page')
    publicaciones = paginator.get_page(page_number)

    if fecha_min and fecha_max:
        publicacion_list = publicacion_list.filter(fecha_gte=fecha_min, fecha_lte=fecha_max)

    if query:
        publicacion_list = publicacion_list.filter(Q(titulo__icontains=query) | Q(contenido__icontains=query))        
   
    return render(request, 'lista_publicaciones.html', {'publicaciones': publicaciones})


def inicio(request):
    return render(request, 'inicio.html')


def agregar_publicacion(request):
    if request.method == 'POST':
        form = PublicacionModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('lista_publicaciones.html', {'form' : form})
    else:
        form = PublicacionModelForm()
    return render(request, 'agregar_publicacion.html', { 'form': form })