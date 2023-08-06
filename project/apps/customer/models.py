from re import U
from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=40, )
    lastname = models.CharField(max_length=40, )
    phone = models.CharField(max_length=20, unique=True)
    email = models.CharField(max_length=50, unique=True)
    date_created = models.DateTimeField(auto_now_add=True, )
    dni = models.CharField(max_length=8, unique=True)
    numero_cliente = models.CharField(max_length=5, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'customer'
