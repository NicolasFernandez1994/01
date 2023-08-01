from dataclasses import field
from django import forms

from . import models


class ProductoCategoriaaForm(forms.ModelForm):
    class Meta:
        model = models.ProductoCategoriaa
        fields = "__all__"
