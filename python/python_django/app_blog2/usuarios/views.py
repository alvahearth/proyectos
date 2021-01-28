from django.shortcuts import redirect, render
from .forms import NewUserForm
from .models import CustomUser
from django.views import View

class RegisterNewUser(View):
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
            return redirect('lista')


        context = {
            'form': form
        }

        return render(request, self.template_name, context)

class ListViewUsers(View):
    template_name = "usuarios/lista.html"

    def get(self, request):
        object_list = CustomUser.objects.all()

        context = {
            'object_list': object_list
        }


        return render(request, self.template_name, context)