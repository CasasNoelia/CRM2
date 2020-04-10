from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuario (models.Model): #Customer
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)




class Tag(models.Model):

    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Empleo(models.Model): #Products

    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Out Door', 'Out Door'),
    )
    name = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=200, null=True,choices=CATEGORY)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    Tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Recibo(models.Model): # Order
    PARTIDA = (
        ('Hs Extras', 'Hs Extras'),
        ('Dia Desc trab', 'Dia Desc trab'),
        ('Feriado', 'Feriado'),
        )
    usuario = models.ForeignKey(Usuario, null=True, on_delete=models.SET_NULL)
    empleo = models.ForeignKey(Empleo, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    partida = models.CharField(max_length=200, null=True, choices=PARTIDA)
    cantidad = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.empleo.name