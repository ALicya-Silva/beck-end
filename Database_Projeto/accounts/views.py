from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CustomAuthenticationForm, CustomUserCreationForm

def login_view(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("login")  # Redireciona para a página inicial
            else:
                # Adiciona mensagem de erro
                messages.error(request, "Credenciais inválidas. Verifique o usuário ou senha.")
    else:
        form = CustomAuthenticationForm()

    return render(request, "registration/login.html", {"form": form})

@login_required
def inicio_view(request):
    """
    Página inicial protegida, acessível apenas para usuários logados.
    """
    return render(request, 'inicio.html')

def logout_view(request):
    """
    Realiza o logout e redireciona para a página de login.
    """
    logout(request)
    return redirect('login')

def cadastrar_view(request):
    """
    View para realizar o cadastro de um novo usuário.
    """
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cadastro realizado com sucesso. Faça login.")
            return redirect('login')
        else:
            messages.error(request, "Erro ao realizar cadastro. Verifique os dados.")
    else:
        form = CustomUserCreationForm()
    return render(request, "register/cadastrar.html", {"form": form})