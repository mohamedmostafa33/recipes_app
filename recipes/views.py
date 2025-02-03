from django.shortcuts import render
from . import models
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
# from django.contrib.auth.decorators import login_required




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

### -- Class based recipes crud operations -- ###
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
    
    
class RecipeUpdateView(UserPassesTestMixin ,LoginRequiredMixin ,UpdateView):
    model = models.Recipe
    template_name = 'recipes/recipe_update.html'
    fields = ['title', 'description', 'image']
    
    def get_success_url(self):
        return reverse_lazy('recipe-detail', kwargs={'pk':self.object.pk})
    
    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author
    
    def handle_no_permission(self):
        messages.error(self.request, 'Error: Only the author of the recipe can edit it.')
        return redirect('recipe-detail', pk=self.get_object().pk)
    

class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Recipe 
    context_object_name = 'recipe'
    template_name = 'recipes/recipe_confirm_delete.html'
    success_url = reverse_lazy('recipes-home')  

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author
    
    def get_success_url(self):
        messages.success(self.request, f"Recipe '{self.get_object().title}' deleted successfully.")
        return super().get_success_url()
            

def about(request):
    return render(request, 'recipes/about.html', {'title' : 'About us'})