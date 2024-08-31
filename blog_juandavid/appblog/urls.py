from django.urls import path
from .views import lista_publicaciones, agregar_publicacion, detalle_publicacion, editar_publicacion

urlpatterns = [
    path('publicaciones/', lista_publicaciones, name='lista_publicaciones'),
    path('agregar_publicacion/', agregar_publicacion, name='agregar_publicacion'),
    path('detalle/<int:pk>/', detalle_publicacion, name='detalle_publicacion'),
    path('editar/<int:pk>/', editar_publicacion, name='editar_publicacion'),
]