from django.shortcuts import render, redirect, get_object_or_404
from .models import Parroquia, Barrio
from .forms import ParroquiaForm, BarrioForm

def index(request):
    return render(request, 'index.html')

def listar_parroquias(request):
    parroquias = Parroquia.objects.all()
    # Para cada parroquia, calculamos total de parques y las profesiones de presidentes para pasarlo al template
    parroquias_data = []
    for p in parroquias:
        barrios = p.barrios.all()
        total_parques = sum(b.num_parques for b in barrios)
        profesiones = []
        for b in barrios:
            presi = b.datos_presidente
            if presi:
                profesiones.append(presi.profesion)
        
        parroquias_data.append({
            'parroquia': p,
            'barrios': barrios,
            'total_parques': total_parques,
            'profesiones': ", ".join(profesiones) if profesiones else "Ninguna",
        })
        
    return render(request, 'listar_parroquias.html', {'parroquias_data': parroquias_data})

def listar_barrios(request):
    barrios = Barrio.objects.all()
    return render(request, 'listar_barrios.html', {'barrios': barrios})

def crear_parroquia(request):
    if request.method == 'POST':
        form = ParroquiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_parroquias')
    else:
        form = ParroquiaForm()
    return render(request, 'formulario_parroquia.html', {'form': form, 'accion': 'Crear'})

def editar_parroquia(request, id):
    parroquia = get_object_or_404(Parroquia, id=id)
    if request.method == 'POST':
        form = ParroquiaForm(request.POST, instance=parroquia)
        if form.is_valid():
            form.save()
            return redirect('listar_parroquias')
    else:
        form = ParroquiaForm(instance=parroquia)
    return render(request, 'formulario_parroquia.html', {'form': form, 'accion': 'Editar'})

def crear_barrio(request):
    if request.method == 'POST':
        form = BarrioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_barrios')
    else:
        form = BarrioForm()
    return render(request, 'formulario_barrio.html', {'form': form, 'accion': 'Crear'})

def editar_barrio(request, id):
    barrio = get_object_or_404(Barrio, id=id)
    if request.method == 'POST':
        form = BarrioForm(request.POST, instance=barrio)
        if form.is_valid():
            form.save()
            return redirect('listar_barrios')
    else:
        form = BarrioForm(instance=barrio)
    return render(request, 'formulario_barrio.html', {'form': form, 'accion': 'Editar'})
