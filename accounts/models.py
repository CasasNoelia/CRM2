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

    def obtener_suma_de_montos(self):
        total_partidas = 0
        recibos_de_este_usuario = Recibo.objects.filter(user=self.user)
        for recibo in recibos_de_este_usuario:
            total_partidas += recibo.monto

        return total_partidas


    def obtener_total_salarios(self):
        total_salarios = 0
        empleos_de_este_usuario = Empleo.objects.filter(user=self.user)
        for empleo in empleos_de_este_usuario:
            total_salarios += empleo.salario

        return total_salarios

    def obtener_total_descuentos(self):
        total_nominal = self.user.usuario.obtener_suma_de_montos()+self.user.usuario.obtener_total_salarios()
        total_descuentos = float(total_nominal)* 0.19625
        return "{: .1f}".format(total_descuentos)

    def obtener_total_cobrar(self):
        total_nominal = self.user.usuario.obtener_suma_de_montos()+self.user.usuario.obtener_total_salarios()
        total_descuentos = float(total_nominal)* 0.19625
        total_cobrar = float(total_nominal) - float(total_descuentos)
        return "{: .1f}".format(total_cobrar)

#total_partidas = sum(monto)
#total_salarios= Sum(salario.empleo)
#total_nominal = total_partidas + total_salarios
#total_descuentos=  total_nominal * 19.625%
#total_cobrar = total_nominal - total_descuentos


class Empleo(models.Model):

    GRUPO = (
        ('Hoteleria-Gastronomia', 'Hoteleria-Gastronomia'),
    )

    User = settings.AUTH_USER_MODEL
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    empresa = models.CharField(max_length=200, null=True)
    grupo = models.CharField(max_length=200, null=True, choices=GRUPO)
    salario = models.IntegerField(null=True)
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
