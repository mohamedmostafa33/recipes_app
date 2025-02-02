from django.shortcuts import render
from . import models
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy



def landing(request):
    return render(request, 'recipes/index.html', {'title' : 'Recipes'})

### -- Function based home view -- ###
# @login_required
# def home(request):
#     recipes = models.Recipe.objects.all()
#     context = {
#         'recipes' : recipes
#     }
#     return render(request ,'recipes/home.html', context)


### -- Class based home view -- ###
class RecipeListView(LoginRequiredMixin, ListView):
    model = models.Recipe
    template_name = 'recipes/home.html'
    context_object_name = 'recipes'


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = models.Recipe
    template_name = 'recipes/recipe_detail.html'
    context_object_name = 'recipe'
    
class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = models.Recipe
    template_name = 'recipes/recipe_create.html'
    fields = ['title', 'description', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('recipe-detail', kwargs={'pk':self.object.pk})

def about(request):
    return render(request, 'recipes/about.html', {'title' : 'About us'})