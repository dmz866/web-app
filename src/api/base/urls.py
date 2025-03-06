from django.urls import path
from . import views
from .views import ListaPendientes, DetalleTarea, CrearTarea

# urlpatterns = [path('', views.lista_pendientes, name='pendientes')]

urlpatterns = [
    path('', ListaPendientes.as_view(), name='pendientes'),
    path('tarea/<int:pk>', DetalleTarea.as_view(), name='tarea'),
    path('crear-tarea/', CrearTarea.as_view(), name='crear-tarea'),
]
