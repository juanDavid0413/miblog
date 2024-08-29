from django.urls import path
from .views import lista_publicaciones, agregar_publicacion, detalle_publicacion

urlpatterns = [
    path('publicaciones/', lista_publicaciones, name='lista_publicaciones'),
    path('agregar_publicacion/', agregar_publicacion, name='agregar_publicacion'),
    path('detalle/<pk>/', detalle_publicacion, name='detalle_publicacion'),
]