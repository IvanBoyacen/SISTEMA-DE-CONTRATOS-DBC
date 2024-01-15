# main/views.py
from django.shortcuts import render
from django.contrib.auth.views import LoginView as AuthLoginView
from django.views import View


class LoginView(AuthLoginView):
    template_name = 'registration/login.html'


def principal(request):
    titulo = "Menu principal"
    context = {
        'titulo': titulo
    }
    return render(request, 'Principal.html', context)

