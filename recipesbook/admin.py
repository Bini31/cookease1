from django.contrib import admin
from recipesbook.models import Recipe
from recipesbook.models import Review
admin.site.register(Recipe)
admin.site.register(Review)