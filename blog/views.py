from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required
# Create your views here.

from .forms import CreateUserForm


@login_required(login_url='blog-login')
def home(request):
    return render(request, 'blog/home.html')


@login_required(login_url='blog-login')
def contactUs(request):
    return render(request, 'blog/contactUs.html')


@login_required(login_url='blog-login')
def shop(request):
    return render(request, 'blog/shop.html')


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('blog-home')
        else:
            messages.info(request, 'username or password is incorrect')
    return render(request, 'blog/login.html')


def logoutUser(request):
    logout(request)
    return redirect('blog-loginPage')


def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for' + user)
            return redirect('blog-login')
    else:
        form = CreateUserForm()
    return render(request, 'blog/register.html', {'form': form})


@login_required(login_url='blog-login')
def product(request):
    return render(request, "blog/product.html")
