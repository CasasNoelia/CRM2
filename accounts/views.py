from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import CreateUserForm
from .forms import OrderForm, Empleo_Form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,   login,  logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,'Cuenta creada con exito por ' + user)
                return redirect('login')

        context = {'form': form}
        return render(request, 'accounts/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Usuario o contraseña incorrecta')

        context = {}
        return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):

    recibos = Recibo.objects.all()
    usuarios = Usuario.objects.get(pk=request.user.id)
    empleos = Empleo.objects.all()


    cantidad = recibos.filter(partida='Hs Extras').count()
    pending = recibos.filter(partida='Feriado').count()

    context = {'recibos': recibos, 'usuarios': usuarios, 'cantidad': cantidad, 'pending': pending,'empleos': empleos}

    return render(request, 'accounts/dashboard.html', context)



@login_required(login_url='login')
def usuario(request, pk_test):
    usuario = Usuario.objects.get(id=pk_test)

    recibos = usuario.order_set.all()
    recibo_count = recibos.count()

    context = {'usuario':usuario,'recibos': recibos, 'recibo_count': recibo_count}
    return render(request, 'accounts/usuario.html', context)


@login_required(login_url='login')
def createRecibo(request):
    form = OrderForm()
    if request.method == 'POST':
            form = OrderForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)

@login_required(login_url='login')
def updateRecibo(request, pk):

    recibo = Recibo.objects.get(id=pk)
    form = OrderForm(instance=recibo)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=recibo)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)


@login_required(login_url='login')
def deleteRecibo(request, pk):
    recibo = Recibo.objects.get(id=pk)
    if request.method == "POST":
        recibo.delete()
        return redirect('/')

    context = {'item': recibo}
    return render(request, 'accounts/delete.html', context)


def Informacion(request):
    return render(request, 'accounts/informacion.html')

@login_required(login_url ='login')
def empleo(request):
    empleos = Empleo.objects.all()
    return render(request,'accounts/empleo.html', {'empleos': empleos})


@login_required(login_url='login')
def createEmpleo(request):

    allempleo = Empleo.objects.all()

    form = Empleo_Form()
    if request.method == 'POST':
        form = Empleo_Form(request.POST)
        if form.is_valid():
            fs = form.save(commit=False)
            fs.user = request.user
            fs.save()
            return redirect('/')

    context = {'form': form, 'allempleo': allempleo}
    return render(request, 'accounts/empleo_form.html', context)



