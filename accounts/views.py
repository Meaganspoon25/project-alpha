from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from accounts.forms import LoginForm

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
