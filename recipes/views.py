from django.shortcuts import render, HttpResponse
from . import models
'''
recipes = [
    {
        'author': 'Alice',
        'title': 'Spaghetti Bolognese',
        'directions': 'Cook spaghetti and prepare the sauce with beef, tomatoes, and herbs.',
        'date_posted': 'Jan 15 2025'
    },
    {
        'author': 'Bob',
        'title': 'Grilled Chicken Salad',
        'directions': 'Grill chicken and serve on a bed of mixed greens with veggies and vinaigrette.',
        'date_posted': 'Jan 18 2025'
    },
    {
        'author': 'Claire',
        'title': 'Vegetable Stir Fry',
        'directions': 'Stir fry vegetables in sesame oil with soy sauce and serve with rice.',
        'date_posted': 'Jan 20 2025'
    },
    {
        'author': 'David',
        'title': 'Chocolate Chip Cookies',
        'directions': 'Mix dough, add chocolate chips, bake at 350°F for 10 minutes.',
        'date_posted': 'Jan 22 2025'
    },
    {
        'author': 'Emily',
        'title': 'Beef Tacos',
        'directions': 'Cook beef with seasoning, fill taco shells with beef, lettuce, and cheese.',
        'date_posted': 'Jan 25 2025'
    }
]
'''

def home(request):
    recipes = models.Recipe.objects.all()
    context = {
        'recipes' : recipes
    }
    return render(request ,'recipes/home.html', context)

def about(request):
    return render(request, 'recipes/about.html', {'title' : 'About us'})