from django.shortcuts import render, redirect
from .forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

# https://swarf00.github.io/2018/12/10/login.html
def sign_in(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            new_user = authenticate(email=form.cleaned_data['email'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'account/sign_in.html', {'form': form})


def info(request):
    if request.user.is_authenticated:
        return render(request, 'account/info.html')
    else:
        return redirect('login')

