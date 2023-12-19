from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from accounts.forms import LoginForm, SignUpForm
from django.contrib.auth.models import User

# Create your views here.
def login_view(request):
    form = LoginForm(request.POST)

    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("home")

    else:
        form = LoginForm()

    return render(request, "accounts/login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("login")

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            password_confirmation = form.cleaned_data["password_confirmation"]

            if password != password_confirmation:
                error = "The passwords do not match"
                return render(request, "accounts/signup.html", {"form": form, "error": error})

            new_user = User.objects.create_user(username=username, password=password)
            login(request, new_user)
            return redirect("list_projects")
    else:
        form = SignUpForm()

    return render(request, "accounts/signup.html", {"form": form})
