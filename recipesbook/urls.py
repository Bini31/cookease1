"""
URL configuration for cookease project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
app_name = 'recipesbook'
from recipesbook import views
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('addrecipes', views.Addrecipe.as_view(), name='addrecipes'),
    path('viewrecipes',views.Viewrecipe.as_view(), name='viewrecipes'),
path('details/<int:i>', views.Detailrecipe.as_view(), name='details'),
path('review/<int:i>', views.ReviewView.as_view(), name='review'),
path('register',views.Register.as_view(), name='register'),
path('login', views.Login.as_view(), name='login'),
    path('logout', views.Logout.as_view(), name='logout'),
]
