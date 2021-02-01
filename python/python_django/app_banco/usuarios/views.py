from django import forms
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
        b = request.user.dinero.dinero
        s = request.user.moverdinero.dinero

        result = b - s

        context = {
            'p_form': p_form,
            'result': result
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
            d_form.save()
            return redirect('perfil')


class Historial(View):
    template_name = "usuarios/historial.html"
    

    def get(self, request, id):
        
        obj = CustomUser.objects.filter(id=id).first()
        

        context = {
            'obj_list': obj
        }

        return render(request, self.template_name, context)
