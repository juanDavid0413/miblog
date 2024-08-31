from datetime import date
from django import forms
from .models import Publicacion
from django.core.exceptions import ValidationError

class PublicacionModelForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['titulo','contenido','fecha_publicacion','categoria','autor']

    def clean_fecha_publicacion(self):
        fecha_publicacion= self.cleaned_data['fecha_publicacion']
        if fecha_publicacion > date.today():
            raise ValidationError('La fecha no puede ser superior a la actual')
        return fecha_publicacion
    
    def clean_titulo(self):
        titulo = self.cleaned_data['titulo']
        if len(titulo) < 5:
            raise ValidationError('Que pensas con ese titulo tan corto, prueba una con minimo 5 digitos')
        if len(titulo) > 200:
            raise ValidationError('Estas loco, ¿mas de 200 digitos?, esto ya es contenido, prueba con un titulo mas corto')
        return titulo


