from django.shortcuts import render, HttpResponseRedirect, reverse
from django.http import HttpResponseForbidden

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from helloapp.models import Author, Recipe
from helloapp.forms import AddRecipeForm, AddAuthorForm, LogInForm

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

@login_required
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
                author = request.user.author,
            )
            return HttpResponseRedirect(reverse("homepage"))
    form = AddRecipeForm()
    return render(request, "generic_form.html", {"form": form})

@login_required
def author_form(request):
    if request.user.is_staff:
        if request.method == "POST":
            form = AddAuthorForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                new_user = User.objects.create_user(username=data.get("username"), password=data.get("password"))
                Author.objects.create(name=data.get("name"), user=new_user)
            return HttpResponseRedirect(reverse("homepage"))
    else:
        return HttpResponseForbidden("You are not authorized to make an author.")
    form = AddAuthorForm()
    return render(request, "generic_form.html", {"form": form}) 

def login_view(request):
    if request.method == "POST":
        form = LogInForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get("username"), password=data.get("password"))
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get("next", reverse("homepage")))
    form = LogInForm()
    return render(request, "generic_form.html", {"form": form})

# def sign_up_view(request):
#     if request.method == "POST":
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             new_user = User.objects.create_user(username=data.get("username"), password=data.get("password"))
#             login(request, new_user)
#             return HttpResponseRedirect(reverse("homepage"))
    
    
#     form = SignUpForm()
#     return render(request, "generic_form.html", {"form": form})
        

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))
    
     