from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Recibo, Empleo


class OrderForm(ModelForm):
    class Meta:
        model = Recibo
        fields = ['partida', 'cantidad']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class Empleo_Form(ModelForm):
    class Meta:
        model = Empleo
        fields = ['empresa', 'salario', 'grupo']
