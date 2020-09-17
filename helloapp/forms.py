from django import forms

from helloapp.models import Author, Recipe

class AddRecipeForm(forms.Form):
    title = forms.CharField(max_length=50)
    instructions = forms.CharField(widget=forms.Textarea)
    description = forms.CharField(widget=forms.Textarea)
    time_required = forms.CharField(max_length=20)

class AddAuthorForm(forms.ModelForm):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Author
        fields = ["name"]
                
class LogInForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)
    
    