from datetime import time
import datetime
from typing import List
from django import forms
from django.forms.widgets import Select
from django.shortcuts import redirect, render
from django.views import View
from .forms import NewUserForm, UpdatePerfil, MakeTransfer
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CustomUser, Dinero, MoverDinero
from django.views.decorators.csrf import requires_csrf_token
from django.utils import timezone
import csv
import os



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
            dinero2 = request.user.moverdinero.dinero
            
            #timezone.UTC()
            q = MoverDinero.objects.filter(id=index).update(fecha_de_movimiento=timezone.now().strftime("%Y-%m-%d %H:%M:%S"))
            q = MoverDinero.objects.filter(id=index).first()
            hora = q.fecha_de_movimiento
            
            Dinero.objects.filter(id=index).update(dinero=(dinero1 - dinero2))
            #MoverDinero.objects.filter(id=index).update(fecha_de_movimiento=timezone.now)
            
            archi = ListaHistorial(list_of_user_transfers[index], dinero2, hora, index)
            archi.appendIndexOrValues()
            d_form.save()
            return redirect('perfil')

class Historial(View):
    template_name = "usuarios/historial.html"
    
    def get(self, request, id):        
        
        with open(f"lista_transferencias{id}.csv", newline="") as csv_file:
            csv_f = csv.reader(csv_file)
            
            cosas = []
            
            for i in csv_f:
                cosas.append((i[1], i[2]))
            
        context = {
            'obj_list': cosas
        }

        return render(request, self.template_name, context)

list_of_user_transfers = [[] for i in range(1,120)]

class ListaHistorial:
    def __init__(self, lists ,value, hora, id):
        self.value = value
        self.id = id
        self.hora = hora
        self.lists = lists
        
    def appendIndexOrValues(self):
        index = str(self.id)
        if len(self.lists) < 1:
            self.lists.append(index)
            self.lists.append((self.value, self.hora))
            
            csv_file_number = self.id
            header = ["id", "Transferido", "Hora"]
            data = [self.id ,self.value ,self.hora]
                    
            with open(f"lista_transferencias{csv_file_number}.csv", mode="w", newline="") as transfer_file:

                transfer_write = csv.writer(transfer_file)
                        
                transfer_write.writerow(header)
                transfer_write.writerow(data)
        else:
            self.lists.append((self.value, self.hora))
            
            for i in range(1,120):
                if i == len(self.lists):
                    data = [self.id ,self.value ,self.hora]
                    
                    with open(f"lista_transferencias{self.id}.csv", mode="a+", newline="") as transfer_file:
                        transfer_write = csv.writer(transfer_file)
                        
                        transfer_write.writerow(data)
            
        return self.lists
    
