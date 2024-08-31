from django.db import models

class Publicacion(models.Model):
    titulo = models.CharField(max_length=150)
    contenido = models.TextField()
    fecha_publicacion = models.DateField()
    categoria = models.CharField(max_length=150)
    autor = models.CharField(max_length=150)

    def __str__(self):
        return str(self.titulo)

