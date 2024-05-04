from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import *

from .models import User


# class createForm(forms.Form):
#     title = forms.CharField(label="Title",widget=forms.TextInput)
#     description = forms.CharField(label="Description", widget=forms.Textarea(attrs={
#         'style' : 'width:100%'}))
#     InitialPrice = forms.FloatField(label="Price(US$)")
#     CHOICES = (('Categoría 1', 'Categoría 1'),('Option 2', 'Option 2'),)
#     category = forms.ChoiceField(widget=forms.Select,choices=CHOICES)
#     image = forms.ImageField(label="Image")
#     class Meta:

def index(request):
    return render(request, "auctions/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
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
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
    
def new_list(request):
    if request.POST:
        form = new_listForm(request.POST)
        if form.is_valid():
        # title = form.cleaned_data["title"]
        # description = form.cleaned_data["description"]
        # InitialPrice = form.cleaned_data["InitialPrice"]
        # category = form.cleaned_data["category"]
        # image = form.cleaned_data["image"]
            print(form)
            form.save()
        return render(request,"auctions/index.html")
    else:
        return render(request,"auctions/new_list.html",{"form": new_listForm(request.POST)})
