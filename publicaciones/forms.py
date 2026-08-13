from django import forms
from .models import Publicacion, Producto

class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ["titulo", "descripcion", "imagen", "publicada"]

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ["nombre", "descripcion", "precio", "imagen", "disponible"]
