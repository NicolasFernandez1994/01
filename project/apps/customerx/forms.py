from dataclasses import field
from django import forms

from . import models


class CustomerxForm(forms.ModelForm):
    class Meta:
        model = models.Customerx
        fields = "__all__"