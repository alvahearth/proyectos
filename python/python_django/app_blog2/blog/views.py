from django import forms
from django.contrib.auth.models import User
from django.db import connection
from django.forms.fields import EmailField
from django.http import request
from django.shortcuts import redirect, render, get_object_or_404, get_list_or_404
from django.views import View
from django.template import RequestContext
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator
from django.contrib import messages
from django.core.mail import EmailMessage, send_mass_mail
from django.core import mail
import csv

import pandas as pd
from pathlib import Path
import os

from .models import (
    Articulo, 
    Category,
    Comments
)

from .forms import (
    NuevoArticulo, 
    EditarArticuloForm,
    ComentarioForm,
    ContactoForm,
    ConfirmarBorrar
)


class ListaDeArticulos(View):
    template_name = "blog/index.html"

    def get(self, request):

        obj = Articulo.objects.all().reverse()
        
        cat = Category.objects.all()

        com = Comments.objects.all().order_by('date_added')

        paginas = Paginator(obj, 3)

        page = request.GET.get('page')

        obj = paginas.get_page(page)

        context = {
            'obj_list': obj,
            'cat_list': cat,
            'com_list': com,
        }
        return render(request, self.template_name, context)

class ListaPorCategoria(View):
    template_name = "blog/index_categoria.html"

    def get(self, request, id):
        obj_category = Category.objects.filter(id=id)
        obj = obj_category.first().articulo_set.all()

        paginas = Paginator(obj, 3)

        page = request.GET.get('page')

        obj = paginas.get_page(page)

        context = {
            'obj_category': obj_category,
            'obj': obj
        }

        return render(request, self.template_name, context)

class CrearNuevoArticulo(LoginRequiredMixin ,View):
    template_name = "blog/form.html"

    def get(self, request):
        form = NuevoArticulo()
        form.fields['user'].initial = request.user
        form.fields['user'].widget = forms.HiddenInput()

        context = {
            'form': form,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = NuevoArticulo(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            algo = form.save(commit=False)
            algo.user = request.user
            algo.save()
            
            return redirect('index')

class EditarArticulo(LoginRequiredMixin, View):
    template_name = "blog/articulo_edit.html"
 
    def get(self, request, id):
        obj = Articulo.objects.get(id=id)
        print(obj)
        f_form = EditarArticuloForm(instance=obj)

        context = {
            'f_form': f_form,
            'obj': obj
        }

        return render(request, self.template_name, context)

    def post(self, request, id):
        obj = Articulo.objects.get(id=id)
        f_form = EditarArticuloForm(request.POST, request.FILES, instance=obj)

        if f_form.is_valid():
            f_form.save()
            return redirect('index')
        else:
            print('error')

class ArticuloDetalle(View):
    template_name = "blog/detail.html"

    def get(self, request, id):
        obj = Articulo.objects.get(id=id)

        context = {
            'obj' : obj
        }

        return render(request, self.template_name, context)

class ArticuloComentario(LoginRequiredMixin ,View):
    template_name = "blog/articulo_comentario.html"

    def get(self, request, id):
        form = ComentarioForm()
        obj = Articulo.objects.get(id=id)
        
        form.fields['name'].initial = request.user
        form.fields['name'].widget = forms.HiddenInput()

        form.fields['articulo'].initial = obj
        form.fields['articulo'].widget = forms.HiddenInput()

        context = {
            'comentario_form': form,
            'obj': obj
        }

        return render(request, self.template_name, context)

    def post(self, request, id):
        form = ComentarioForm(request.POST)

        if form.is_valid():
            form.save()
            algo = form.save(commit=False)
            algo.user = request.user
            algo.save()

            return redirect('index')


class BorrarArticulo(LoginRequiredMixin, UserPassesTestMixin,View):
    template_name = "blog/confirmar_borrar.html"

    def test_func(self):
        print(dir(self.request.user.articulo_set))
        print(self.request.user.articulo_set.first().user)
        
        if self.request.user == self.request.user.articulo_set.first().user:
            return True
        return False

    def get(self, request, id):
        obj = Articulo.objects.get(id=id)
        form = ConfirmarBorrar()

        context = {
            'obj': obj,
            'confirm_form': form
        }

        return render(request, self.template_name, context)

    def post(self, request, id):
        obj = Articulo.objects.get(id=id)
        form = ConfirmarBorrar(request.POST)

        obj.delete()
        return redirect('perfil')

# # # # # # #
# Class base contact view doesn't work with heroku, need fix #

# class ContactoInfo(View):
#     template_name = "blog/contacto.html"
#     def get(self, request):
#         form = ContactoForm()
#         context = {
#             'form': form
#         }
#         return render(request, self.template_name, context)
#     def post(self, request):
#         form = ContactoForm(request.POST)
#         context = {}
#         if form.is_valid():            
#             nombre = form.cleaned_data.get('nombre')
#             rut = form.cleaned_data.get('rut')
#             email = form.cleaned_data.get('email')
#             telefono = form.cleaned_data.get('telefono')
#             comentario = form.cleaned_data.get('comentario')
#             contacto = ListaDeContactos(nombre, rut, email, telefono, comentario, lista)
#             contacto.agregar_nuevo_contacto()
#             messages.success(request, "Gracias por confiar en nosotros, te contactaremos lo antes posible")
#             return redirect('contacto')
#         context = {
#             'form': form
#         }
#         return render(request, self.template_name, context)

# # # # # # #

def contacto_info(request):
    form = ContactoForm()
    context = {}

    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get('nombre')
            rut = form.cleaned_data.get('rut')
            email = form.cleaned_data.get('email')
            telefono = form.cleaned_data.get('telefono')
            comentario = form.cleaned_data.get('comentario')

            contacto = ListaDeContactos(nombre, rut, email, telefono, comentario, lista)
            contacto.agregar_nuevo_contacto()
            messages.success(request, "Gracias por confiar en nosotros, te contactaremos lo antes posible")
            return redirect('contacto')

    context = {
        'form': form
    }

    return render(request, "blog/contacto.html", context)
        

lista = []


class ListaDeContactos:
    def __init__(self, nombre, rut, email, telefono, comentario , lista):
        self.nombre = nombre
        self.rut = rut
        self.email = email
        self.telefono = telefono
        self.comentario = comentario
        self.lista = lista


    def agregar_nuevo_contacto(self):

        headers = ['nombre', 'rut', 'email', 'telefono', 'comentario']
        data = [self.nombre, self.rut, self.email, self.telefono, self.comentario]
        if len(lista) < 1:
            self.lista.append(data)
            with open('contactos.csv', 'w') as csv_file:
                csv_file_writer = csv.writer(csv_file, delimiter=",")

                csv_file_writer.writerow(headers)
                csv_file_writer.writerow(data)

        else:
            self.lista.append(data)
            with open('contactos.csv', 'a') as csv_file:
                csv_file_writer = csv.writer(csv_file, delimiter=",")

                csv_file_writer.writerow(data)
        
        BASE_DIR = Path(__file__).resolve().parent.parent
        df = pd.read_csv(os.path.join(f'{BASE_DIR}/', 'contactos.csv'), encoding="ISO 8859-1")
        writer = pd.ExcelWriter('contactos.xlsx')
        df.to_excel(writer, index=False)
        writer.save()   
        
        conexion = mail.get_connection()
        conexion.open()

        email_to_user = EmailMessage(
            subject="Hemos recibido tus datos",
            body="Tus datos han sido registrados y enviados exitosamente a nuestros servidores, te contactaremos dentro de 5 días hábiles",
            from_email="raul.c.pruebas@gmail.com",
            to=[self.email],
        )

        email_to_admin = EmailMessage(
            subject='Contactos_actualizados',
            body='Un nuevo usuario ha enviado sus datos',
            from_email='raul.c.pruebas@gmail.com',
            to=['raul.c.pruebas@gmail.com'],        
        )
        email_to_admin.attach_file(os.path.join(BASE_DIR, "contactos.xlsx"))

        conexion.send_messages([email_to_admin, email_to_user])

        conexion.close()
        
        return self.lista

def error_404(request, response=None):
    context = {}
    return render(request, "blog/error_500.html", context)
                                  

def error_500(request):
    context = {}
    return render(request, "blog/error_500.html", context)