from django.shortcuts import render
from . import models
from django.contrib.auth.decorators import login_required


def landing(request):
    return render(request, 'recipes/index.html', {'title' : 'Recipes'})


@login_required
def home(request):
    recipes = models.Recipe.objects.all()
    context = {
        'recipes' : recipes
    }
    return render(request ,'recipes/home.html', context)

def about(request):
    return render(request, 'recipes/about.html', {'title' : 'About us'})