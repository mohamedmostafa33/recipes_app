from django.shortcuts import render, HttpResponse

recipes = [
    {
        'author' : 'Jon',
        'title' : 'Cheese cake',
        'directions' : 'mix all things',
        'date_posted' : 'Jan 30 2025'
    },
    {
        'author' : 'Jon',
        'title' : 'Pizza',
        'directions' : 'mix all things',
        'date_posted' : 'Jan 25 2025'
    },
    {
        'author' : 'Jon',
        'title' : 'Burger',
        'directions' : 'mix all things',
        'date_posted' : 'Jan 11 2025'
    }
]

def home(request):
    context = {
        'recipes' : recipes
    }
    return render(request ,'recipes/home.html', context)

def about(request):
    return render(request, 'recipes/about.html', {'title' : 'Recipes | About us'})