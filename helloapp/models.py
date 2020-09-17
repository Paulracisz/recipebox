from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=80)
    bio = models.TextField(max_length=300, default='Enter text here!')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorites = models.ManyToManyField("Recipe", symmetrical=False, related_name= "favorites")
    
    def __str__(self):
        return self.name

    
class Recipe(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    time_required = models.CharField(max_length=20)
    instructions = models.TextField()
    
    def __str__(self):
        return f"{self.title}-{self.author.name}"
    