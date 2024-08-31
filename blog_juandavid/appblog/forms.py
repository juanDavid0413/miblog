from django import forms
from .models import Publicacion

class PublicacionModelForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['titulo','contenido','fecha_publicacion','categoria','autor']


