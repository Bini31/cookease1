from recipesbook.models import Recipe,Review
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields ='__all__'
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','password1','password2','email','first_name','last_name')
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields =['rating','comments']