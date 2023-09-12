from django.db import models
from django.utils import timezone


# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    stock = models.IntegerField()
    puntaje = models.FloatField()
    # CASCADA: ELIMINAR PRODUCTO
    # PROTECT: LANZA UN ERROR
    # RESTRICT: SOLO ELIMINA SI NO EXISTEN PRODUCTOS
    # SET_NULL: ACTUALIZA A VALOR NULO
    # SET_DEFAULT: DESIGNA VALOR POR DEFECTO
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    creado_en = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre
