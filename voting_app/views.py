from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from voting_app.models import User


def index(request):
    return render(request, 'voting_app/vote.html')


def login_view(request):
    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        firstname = request.POST["firstname"]
        secondname = request.POST["secondname"]
        thirdname = request.POST["thirdname"]
        birth_date = request.POST["birth_date"]

        identification = request.POST["identification"]
        confirmation = request.POST["confirmation"]
        if identification != confirmation:
            return render(request, "voting_app/register.html", {
                "message": "Passwords must match."
            })

        try:
            user = User.objects.create_user(firstname, secondname, thirdname)
            user.birth_date = birth_date
            user.save()
        except IntegrityError:
            return render(request, "voting_app/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "voting_app/register.html")
