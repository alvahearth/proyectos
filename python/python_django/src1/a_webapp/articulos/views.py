from django.shortcuts import render, redirect
from django.views import View
from .forms import NuevoArticulo
from .models import Articulo
from django.contrib import messages

class RegistrarNuevoArticulo(View):
    template_name = "articulos/submit.html"
    
    def get(self, request):
        form = NuevoArticulo
        
        context = {
            'form': form
        }
        
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = NuevoArticulo(request.POST)
        context = {}
        
        if form.is_valid():
            info = form.cleaned_data.get('titulo')
            form.save()
            
            context = {
                'form': form
            }
            messages.success(request, f"El articulo '{info}' fue creado exitosamente")
            return redirect('lista')
            
        return render(request, self.template_name, context)
    
class ArticulosSistema(View):
    template_name = "articulos/index.html"
    
    def get(self, request):
        object_list = Articulo.objects.all()
        
        context = {
            'obj_list': object_list
        }
        
        return render(request, self.template_name, context)
