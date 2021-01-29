from django.shortcuts import render
from .forms import NewUserForm
#from django.contrib.auth.models import User
from .models import CustomUser
from django.views import View

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
            
        context = {
            'form': form
        }
        
        return render(request, self.template_name, context)

# Create your views here.
