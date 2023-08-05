from django import forms

from .models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["nombre", "apellido", "nacimiento", "dni", "numero_customer"]