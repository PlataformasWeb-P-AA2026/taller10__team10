from django import forms
from .models import Parroquia, Barrio

class ParroquiaForm(forms.ModelForm):
    class Meta:
        model = Parroquia
        fields = ['nombre', 'ubicacion', 'tipo']

class BarrioForm(forms.ModelForm):
    class Meta:
        model = Barrio
        fields = ['nombre', 'num_viviendas', 'num_parques', 'num_edificios', 'parroquia']
