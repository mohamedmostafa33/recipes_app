from django.shortcuts import render, redirect
from django.contrib import messages
from . import forms

def register(request):
    if request.method == 'POST':
        form = forms.UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f"'{username}', you're account has been created!")
            return redirect("recipes-home")
        else:
            messages.error(request, "There was an error with your registration. Please check the form.")
    else:
        form = forms.UserRegisterForm()
    return render(request, 'users/register.html', {'form' : form , 'title' : 'Register'})