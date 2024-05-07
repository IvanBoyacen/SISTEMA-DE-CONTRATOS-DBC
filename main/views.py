# main/views.py
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView


@login_required
def principal(request):
    titulo = "Menu principal"
    context = {
        'titulo': titulo
    }
    return render(request, 'Principal.html', context)

@login_required
def mostrar_perfil(request):
    usuario = request.user
    context = {
        'usuario': usuario
    }
    return render(request, 'perfil/perfil.html', context)

def recuperar_contrasena(request):
    return render(request, 'registration/olvide-contraseña.html')

def logout_usuario(request):
    logout(request)
    return redirect('login')
class CustomLogoutView(LogoutView):
    next_page = '/accounts/login/'

