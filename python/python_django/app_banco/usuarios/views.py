from typing import List
from django import forms
from django.forms.widgets import Select
from django.shortcuts import redirect, render
from django.views import View
from .forms import NewUserForm, UpdatePerfil, MakeTransfer
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CustomUser, Dinero, MoverDinero




class HomePage(View):
    template_name = "usuarios/inicio.html"
    
    def get(self, request):
        year = 2021

        hasta = range(year,2023)

        context = {
            'años': hasta
        }
        return render(request, self.template_name, context)


class RegisterUser(View):
    template_name = "usuarios/registro.html"

    def get(self, request):
        form = NewUserForm()

        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = NewUserForm(request.POST)
        context = {}

        if form.is_valid():
            form.save()
            return redirect('login')
        
        context = {
            'form': form
        }

        return render(request, self.template_name, context)


class Profile(LoginRequiredMixin, View):
    template_name = "usuarios/perfil.html"

    def get(self, request):
        p_form = UpdatePerfil(instance=request.user.profile)
        index = request.user.id

        context = {
            'p_form': p_form,
            'result': Dinero.objects.filter(id=index).first()
        }

        return render(request, self.template_name, context)

    def post(self, request):
        p_form = UpdatePerfil(request.POST, request.FILES, instance=request.user.profile)

        if p_form.is_valid():
            p_form.save()
            return redirect('perfil')



class Transaction(View):
    template_name = "usuarios/transferencia.html"

    def get(self, request):
        d_form = MakeTransfer()

        context = {
            'd_form': d_form
        }

        return render(request, self.template_name, context)

    def post(self, request):
        d_form = MakeTransfer(request.POST, instance=request.user.moverdinero)
        
        
        if d_form.is_valid():
            index = request.user.id
            dinero1 = request.user.dinero.dinero
            print(dir(MakeTransfer(instance=request.user.moverdinero)))
            dinero2 = request.user.moverdinero.dinero
            
            
            Dinero.objects.filter(id=index).update(dinero=(dinero1 - dinero2))
            archi = ListaHistorial(historial_transferencias, dinero2, index)
            archi.appendIndexOrValues()
            d_form.save()
            return redirect('perfil')


class Historial(View):
    template_name = "usuarios/historial.html"
    

    def get(self, request, id):
            
        context = {
            'obj_list': historial_transferencias
        }

        return render(request, self.template_name, context)

historial_transferencias = []
class ListaHistorial:
    def __init__(self, lists ,value, id):
        self.value = value
        self.id = id
        self.lists = lists
        
    def appendIndexOrValues(self):
        index = str(self.id)
        if len(self.lists) < 1:
            self.lists.append(index)
            self.lists.append(self.value)
        else:
            self.lists.append(self.value)
            
        return self.lists