from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})
    context = {
        "user": request.user
    }
    return render(request, "orders/menu.html", context)
    
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
            return render(request, "orders/login.html", {"message": "Login error: Invalid credentials."})
    else:
        return HttpResponseRedirect(reverse("index"))

def logout_view(request):
    logout(request)
    return render(request, "orders/login.html", {"message": "Logged out."})