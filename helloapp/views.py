from django.shortcuts import render, HttpResponseRedirect, reverse

from helloapp.models import Author, Recipe

from helloapp.forms import AddRecipeForm, AddAuthorForm

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

def recipe_form(request):
    if request.method == "POST":
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title = data.get("title"),
                instructions = data.get("instructions"),
                description = data.get("description"),
                time_required = data.get("time_required"),
                author = data.get("author"),
            )
            return HttpResponseRedirect(reverse("homepage"))
    form = AddRecipeForm()
    return render(request, "generic_form.html", {"form": form})

def author_form(request):
    if request.method == "POST":
        form = AddAuthorForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse("homepage"))
    form = AddAuthorForm()
    return render(request, "generic_form.html", {"form": form}) 
    
     