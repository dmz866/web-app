from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Tarea


# def lista_pendientes(pedido):
# return HttpResponse('Shi')

class ListaPendientes(ListView):
    model = Tarea
    context_object_name = 'tareas'

class DetalleTarea(DetailView):
    template_name = 'base/tarea.html' #tarea_detail.html
    model = Tarea
    context_object_name = 'tarea'

class CrearTarea(CreateView):
    model = Tarea
    fields = '__all__' #Show all fields
    success_url = reverse_lazy('tareas')

class EditarTarea(UpdateView):
    model = Tarea
    fields = '__all__' #Show all fields
    success_url = reverse_lazy('tareas')

class EliminarTarea(DeleteView):
    model = Tarea
    context_object_name = 'tarea'
    success_url = reverse_lazy('tareas')