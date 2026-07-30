from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('parroquias/', views.listar_parroquias, name='listar_parroquias'),
    path('parroquias/crear/', views.crear_parroquia, name='crear_parroquia'),
    path('parroquias/editar/<int:id>/', views.editar_parroquia, name='editar_parroquia'),
    path('barrios/', views.listar_barrios, name='listar_barrios'),
    path('barrios/crear/', views.crear_barrio, name='crear_barrio'),
    path('barrios/editar/<int:id>/', views.editar_barrio, name='editar_barrio'),
]
