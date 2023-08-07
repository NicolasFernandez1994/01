from django.db import models

# Create your models here.
class Work(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    trabajo = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    descripcion = models.TextField(max_length=250)
    imagen = models.ImageField(upload_to='productos/')

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'work'