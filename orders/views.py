from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template.defaulttags import register

from .models import Pizza, PizzaCrust, PizzaStyle, PizzaSize, PizzaTopping

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})
    return HttpResponseRedirect(reverse("menu"))

    
def login_view(request):
    if (request.method == "POST" and
        "username" in request.POST and
        "password" in request.POST):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            context = {"message": "Login error: Invalid credentials."}
            return render(request, "orders/login.html", context)
    else:
        return HttpResponseRedirect(reverse("index"))

def logout_view(request):
    logout(request)
    context = {"message": "Logged out."}
    return render(request, "orders/login.html", context)

def menu_view(request):
    pizzas_qs = Pizza.objects.all()
    crusts = PizzaCrust.objects.all().order_by("sort_order")
    styles = PizzaStyle.objects.all().order_by("sort_order")
    sizes = PizzaSize.objects.all().order_by("sort_order")
    toppings = PizzaTopping.objects.all().order_by("name")
    pizzas = {}
    for crust in crusts:
        pizzas[crust.name] = {}
        for style in styles:
            pizzas[crust.name][style.name] = {}
            for size in sizes:
                pizzas[crust.name][style.name][size.name] = {}
                pizzas[crust.name][style.name][size.name]["id"] = pizzas_qs.filter(crust__name=crust.name
                    , style__name = style.name
                    , size__name = size.name
                    )[0].id
                pizzas[crust.name][style.name][size.name]["price"] = pizzas_qs.filter(crust__name=crust.name
                    , style__name = style.name
                    , size__name = size.name
                    )[0].price
                pizzas[crust.name][style.name][size.name]["free_toppings"] = range(styles.filter(name=style.name)[0].free_toppings)


    context = {
        "user" : request.user ,
        "pizzas" : pizzas ,
        "crusts" : crusts ,
        "styles" : styles ,
        "sizes" : sizes ,
        "toppings" : toppings
    }
    print(pizzas)
    print(sizes)
    return render(request, "orders/menu.html", context)
