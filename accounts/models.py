from decimal import Decimal
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Usuario(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    empleo = models.ForeignKey(to='Empleo', null=True, on_delete=models.CASCADE)

    def obtener_suma_de_sueldos(self):
        total_mis_sueldos = 0
        mis_empleos = models.Empleo(user=self.pk)
        for empleo in mis_empleos:
            total_mis_sueldos += empleo.salario

        return total_mis_sueldos



class Empleo(models.Model):

    GRUPO = (
        ('Hoteleria-Gastronomia', 'Hoteleria-Gastronomia'),
    )

    User = settings.AUTH_USER_MODEL
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    empresa = models.CharField(max_length=200, null=True)
    grupo = models.CharField(max_length=200, null=True, choices=GRUPO)
    salario = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.empresa

    def obtener_valor_dia(self):
        return round(Decimal(self.salario) / 30, 2)

    def obtener_valor_hora(self):
        return round(self.obtener_valor_dia() / 8, 2)



class Recibo(models.Model):
    PARTIDA = (
        ('Hs Extras', 'Hs Extras'),
        ('Hs Dia Desc Trab', 'Hs Dia Desc Trab'),
        ('Feriado', 'Feriado'),
    )

    User = settings.AUTH_USER_MODEL
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    empleo = models.ForeignKey(Empleo, null=True, on_delete=models.SET_NULL)
    partida = models.CharField(max_length=200, null=True, choices=PARTIDA)
    cantidad = models.CharField(max_length=200, null=True)
    fecha_ingreso = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.partida

    @property
    def monto(self):
        if self.empleo:
            return Decimal(self.cantidad) * (self.empleo.obtener_valor_hora())

        else:
            return 0
