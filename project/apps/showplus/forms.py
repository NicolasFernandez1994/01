from django import forms
from .models import Showplus


class ShowplusForm(forms.ModelForm):
    class Meta:
        model = Showplus
        fields = ['nombre', 'apellido', 'telefono', 'descripcion', 'precio', 'imagen']
