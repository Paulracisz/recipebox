"""hello_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from helloapp import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('recipe/<int:recipe_id>/',views.recipe_details, name = "recipeDetails"),
    path('editrecipe/<int:recipe_id>/',views.edit_recipe),
    path('author/<int:author_id>/',views.author_details),
    path('addrecipe/', views.recipe_form, name='newrecipe'),
    path('addauthor/', views.author_form, name='newauthor'),
    path('addfavorite/<int:recipe_id>/', views.add_favorite),
    path('favorites/<int:author_id>/', views.favortie_recipes),
    path('login/', views.login_view, name='loginview'),
    path('logout/', views.logout_view, name='logoutview'),
    path('admin/', admin.site.urls),
]
