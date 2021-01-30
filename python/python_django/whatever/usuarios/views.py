from django.forms.widgets import Select
from django.shortcuts import redirect, render
from .forms import NewUserForm, UpdataUserImage
#from django.contrib.auth.models import User
from .models import CustomUser, PerfilModel
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class UserRegistration(View):
    template_name = "usuarios/registro.html"
    
    def get(self, request):
        form = NewUserForm()
        
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = NewUserForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('login')

class ListUsers(View):
    template_name = "usuarios/lista.html"

    def get(self, request):
        obj = CustomUser.objects.all()

        context = {
            'obj_list': obj
        }
        return render(request, self.template_name, context)


class Profile(LoginRequiredMixin, View):
    template_name = "usuarios/perfil.html"
    
    def get(self, request):
        u_form = UpdataUserImage(instance=request.user.perfilmodel)
        
        context = {
            'form': u_form,
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        u_form = UpdataUserImage(request.POST, request.FILES,instance=request.user.perfilmodel)
        
        if u_form.is_valid():
            u_form.save()
            return redirect('perfil')