from django.shortcuts import redirect, render
from .forms import NewUserForm
#from django.contrib.auth.models import User
from .models import CustomUser
from django.views import View
from django.contrib.auth.decorators import login_required


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
        context = {}
        
        if form.is_valid():
            form.save()
            return redirect('login')
            
        context = {
            'form': form
        }
        
        return render(request, self.template_name, context)

class ListUsers(View):
     template_name = "usuarios/lista.html"

     def get(self, request):
        obj = CustomUser.objects.all()

        context = {
            'obj_list': obj
        }
        return render(request, self.template_name, context)

@login_required(login_url='login/')
def profile(request):
    return render(request, "usuarios/perfil.html")