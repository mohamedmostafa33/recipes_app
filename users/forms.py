from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget= forms.TextInput(attrs={'placeholder' : 'Your Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder' : 'Your Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' : 'You Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' : 'Repeat Password'}))


    class Meta:
        model = User
        fields = [
            'username',
            'email', 
            'password1', 
            'password2'
        ]