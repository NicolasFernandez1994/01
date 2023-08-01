from django.db import models


class ProductoCategoriaa(models.Model):
    """Categoria de productos"""
    articulo = models.CharField(max_length=70, unique=True)
    marca = models.CharField(max_length=70, unique=True)
    codigo = models.CharField(max_length=40, null=True, blank=True)
    descripcion = models.CharField(
        max_length=270, null=True, blank=True, verbose_name="descripcion")

    def __str__(self):
        return self.articulo

    class Meta:
        verbose_name = "Categoria de productoss"
        verbose_name_plural = "Categorias de productoss"
