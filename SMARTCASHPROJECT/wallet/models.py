from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.usuario.__str__()} - {self.nombre}'


class Movimiento(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=10)
    valor = models.IntegerField()
    fecha = models.DateField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.categoria.usuario.__str__()} - {self.nombre}'


class Meta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    fecha_creacion = models.DateField(null=True, blank=True)
    cantidad_meta = models.IntegerField()
    cantidad_actual = models.IntegerField()
    dias_estimados = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.usuario.__str__()} - {self.nombre}'


class EventoFijo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    cantidad = models.IntegerField()

    def __str__(self):
        return f'{self.usuario.__str__()} - {self.nombre}'


class EventoPeriodico(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    dia = models.IntegerField()
    cantidad = models.IntegerField()

    def __str__(self):
        return f'{self.usuario.__str__()} - {self.nombre}'