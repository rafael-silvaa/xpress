from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Reservation, Contact
from .forms import ReservationForm, ContactForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .decorators import custom_login_required


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def menu(request):
    return render(request, 'menu.html')


def handleLogin(request):
    if request.method == "POST":
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.warning(request, "Credenciais inválidas. Por favor, tente novamente.")
            return render(request, 'login.html')

    return render(request, 'login.html')


@custom_login_required
def handleLogout(request):
    logout(request)
    return redirect('index')


def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')

        if password != password1:
            messages.error(request, "As palavras-passe não correspondem. Tente novamente.")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Este nome de utilizador já existe. Escolha outro.")
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = f_name
        user.last_name = l_name
        user.phone = phone
        user.save()

        return redirect('registerSuccess')
    else:
        return render(request, 'register.html')

def register_success(request):
    return render(request, 'register-success.html')


@custom_login_required
def reserve(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'A sua reserva foi efetuada!')
            return redirect('Reserve') # redirect to prevent resub
        else:
            messages.error(request, 'Houve um error ao reservar, tente novamente.')
    else: 
        form = ReservationForm()
    return render(request, 'reserve.html', {'form': form})


@custom_login_required
def user_profile(request):
    user = request.user
    return render(request, 'account.html', {'user': user})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'A sua mensagem foi enviada. Obrigado!')
            return redirect('ContactUs')
        else:
            messages.error(request, 'Houve um erro ao enviar a sua mensagem, tente novamente.')
    else:
        form = ContactForm()
    return render(request, 'about.html')


