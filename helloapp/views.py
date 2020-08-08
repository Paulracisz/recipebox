from django.shortcuts import render

from helloapp.models import Author, Recipe

# Create your views here.
def index(request):
    recipe = Recipe.objects.all()
    return render(request,"index.html", {"recipes": recipe, "welcome": "Welcome to the recipe land!"})

def recipe_details(request, recipe_id):
    recipe = Recipe.objects.filter(id=recipe_id).first()
    return render(request, "recipe.html", {"recipes": recipe})

def author_details(request, author_id):
    author = Author.objects.filter(id=author_id).first()
    owned_recipes = Recipe.objects.filter(author=author)
    return render(request, "author.html", {"authors": author, "own_recipe": owned_recipes})
    
     