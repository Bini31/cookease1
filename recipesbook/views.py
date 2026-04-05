
from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages
from recipesbook.forms import RecipeForm,SignUpForm,LoginForm,ReviewForm
from recipesbook.models import Recipe,Review
from django.contrib.auth import authenticate,login,logout
# Create your views here.
class Home(View):
    def get(self, request):
        return render(request, "home.html")
class Addrecipe(View):
    def get(self, request):
        form_instance=RecipeForm()
        context={'form':form_instance}
        return render(request, "addrecipes.html",context)

    def post(self, request):
        form_instance = RecipeForm(request.POST,request.FILES)
        if form_instance.is_valid():
            form_instance.save()

            return redirect('recipesbook:home')
class Viewrecipe(View):
    def get(self, request):
        r = Recipe.objects.all()

        context = {'recipes': r}

        return render(request, "viewrecipes.html",context)
class Detailrecipe(View):
    def get(self,request,i):
        r = Recipe.objects.get(id=i)
        u = request.user
        rev= Review.objects.filter(username=u)

        context = {'recipes': r,'users':u,'reviews':rev}
        return render(request, "details.html", context)
class Register(View):
    def get(self, request):
        form_instance = SignUpForm()
        context = {'form': form_instance}
        return render(request, "register.html", context)

    def post(self, request):
        form_instance = SignUpForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return render(request, "home.html")
class ReviewView(View):

            def get(self, request,i):
                form_instance = ReviewForm()
                context = {'form': form_instance}
                return render(request, "review.html", context)

            def post(self, request, i):
                form_instance = ReviewForm(request.POST)
                if form_instance.is_valid():
                    review = form_instance.save(commit=False)
                    u = request.user
                    review.username = u

                    rec = Recipe.objects.get(id=i)
                    review.recipe=rec
                    review.save()
                    return redirect('recipesbook:viewrecipes')
class Login(View):
    def post(self, request):
        form_instance = LoginForm(request.POST)
        if form_instance.is_valid():
            data = form_instance.cleaned_data
            print(data)
            u = data['username']
            p = data['password']
            user = authenticate(username=u, password=p)
            if user:
                login(request, user)
                return render(request, "home.html")
            else:
                messages.error(request, "Invalid credentials")
                return redirect('recipesbook:login')

    def get(self, request):
        form_instance = LoginForm()
        context = {'form': form_instance}
        return render(request, "login.html", context)
class Logout(View):
    def get(self, request):
      logout(request)
      return render(request, "home.html")