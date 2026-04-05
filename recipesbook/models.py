from django.contrib.auth.models import User
from django.db import models

class Recipe(models.Model):
    recipename = models.CharField(max_length=100)
    ingredients= models.TextField()
    instructions= models.TextField()
    image = models.ImageField(upload_to='recipes')
    cusine=models.CharField(max_length=50)
    mealtype=models.CharField(max_length=50)
class Review(models.Model):
    rating=models.IntegerField()
    comments=models.TextField()
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    recipe=models.ForeignKey(Recipe,on_delete=models.CASCADE,related_name='reviews')

