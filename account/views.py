from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, template_name="index.html")
    else:
        form = UserCreationForm()
    return render(request, "account/signup.html", {"form": form})

def signin(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            if "next" in request.POST:
                return redirect(request.POST.get("next"))

            return HttpResponse(form.is_valid())

    else:
        form = AuthenticationForm()

    return render(request, 'account/signin.html', {'form': form})

def signout(request):
    if "next" in request.POST:
        logout(request)
        return redirect(request.POST.get("next"))

    else:
        logout(request)
        return redirect("home")
