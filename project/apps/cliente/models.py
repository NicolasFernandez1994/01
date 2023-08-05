from pyexpat import model
from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacimiento = models.DateField()
    dni = models.CharField(max_length=8, unique=True)
    numero_cliente = models.AutoField(primary_key=True, unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
