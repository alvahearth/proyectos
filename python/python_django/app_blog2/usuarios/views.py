from django.core import paginator
from django.shortcuts import redirect, render
from django.urls.conf import path
from django.views import View
from django.contrib.auth.models import User
from .forms import (
    RegisterNewUser, 
    ActualizarDatos,
    ActualizarFoto,
    ActualizardSobreMi
)
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from blog.models import Articulo, Category, Comments
from django.core.paginator import Paginator


# # # # # # # 
# class based register view doesn't work correctly with heroku, need fix #

# class NuevoUsuario(View):
#     template_name = "usuarios/registro.html"
#     def get(self, request):
#         form = RegisterNewUser()
#         context = {
#             'form': form
#         }
#         return render(request, self.template_name, context)
#     def post(self, request):
#         form = RegisterNewUser()
#         aform = RegisterNewUser(request.POST)
#         if aform.is_valid():
#             aform.save()
#             username = aform.cleaned_data.get('username')
#             messages.success(request, f"Tu usuario con el nombre {username} ha sido creado exitosamente")
#             return redirect('login')
#         else:
#             return render(request, self.template_name, {'form': form})

# # # # # # #

def nuevo_usuario(request):
    form = RegisterNewUser()
    context = {}

    if request.method == "POST":
        form = RegisterNewUser(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Tu usuario con el nombre {username} ha sido creado exitosamente")
            return redirect('login')

    context = {
        'form': form
    }

    return render(request, "usuarios/registro.html", context)

class PerfilUsuario(LoginRequiredMixin, View):
    template_name = "usuarios/perfil.html"

    def get(self, request):
        
        obj_list = Articulo.objects.filter(user_id=request.user.id)
        com_list = Comments.objects.filter(name=request.user)

        paginas = Paginator(obj_list, 6)

        page = request.GET.get('page')

        obj_list = paginas.get_page(page)

        context = {
            'obj_list': obj_list,
            'com_list': com_list
        }
        return render(request, self.template_name, context)

    def post(self, request):
        email_form = ActualizarDatos(request.POST, instance=request.user)

        if email_form.is_valid():
            email_form.save()
            return redirect('perfil')

class ActualizarPerfil(LoginRequiredMixin, UserPassesTestMixin, View):
    template_name = "usuarios/actualizar_perfil.html"

    def test_func(self):
        if self.request.user == self.request.user.perfildelusuario.user:
            return True
        return False

    def get(self, request):
        datos_form = ActualizarDatos(instance=request.user)
        foto_form = ActualizarFoto(instance=request.user.perfildelusuario)
        aboutme_form = ActualizardSobreMi(instance=request.user.perfildelusuario)
        
        context = {
            'datos_form': datos_form,
            'foto_form': foto_form,
            'aboutme_form': aboutme_form
        }

        return render(request, self.template_name, context)

    def post(self, request):
        datos_form = ActualizarDatos(request.POST, instance=request.user)
        foto_form = ActualizarFoto(request.POST, request.FILES, instance=request.user.perfildelusuario)
        aboutme_form = ActualizardSobreMi(request.POST, instance=request.user.perfildelusuario)

        if datos_form.is_valid() and foto_form.is_valid() and aboutme_form.is_valid():
            datos_form.save()
            foto_form.save()
            aboutme_form.save()
            return redirect('perfil')