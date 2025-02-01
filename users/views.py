from django.shortcuts import render, redirect
from django.contrib import messages
from . import forms
from django.contrib.auth import authenticate, login, logout

def register(request):
    if request.method == 'POST':
        form = forms.UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f"'{username}', you're account has been created, Please Login.")
            return redirect("user-login")
        else:
            messages.error(request, "There was an error with your registration. Please check the form.")
    else:
        form = forms.UserRegisterForm()
    return render(request, 'users/register.html', {'form' : form , 'title' : 'Register'})


def user_login(request):
    if request.method == 'POST':
        form = forms.UserLoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request , f"Welcome, { user.username }!")
                return redirect("recipes-home")
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Please Enter a correct username and password. Note that both fields may be case sensitive.")
    else:
        form = forms.UserLoginForm()
    
    return render(request, 'users/login.html', {'form': form, 'title' : 'Login'})


def user_logout(request):
    logout(request)
    
    messages.success(request, "You have been logged out successfully.")

    return render(request, 'users/logout.html')