from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import *


# Create your views here.
def home(request):
    return render(request, "home.html", {})


def about_site(request):
    return render(request, "about_site.html")


def agents(request):
    agents_list = Agents.objects.all()

    return render(request, "agents.html", {'agents_list': agents_list})


def collaboration_api(request):
    if request.method == 'POST':
        agency_name = request.POST.get('agency_name')
        agency_url = request.POST.get('agency_url')
        phone_number = request.POST.get('phone_number')

        AgencyRequests.objects.create(title=agency_name, url=agency_url, phone_number=phone_number)

        return redirect("success/")

    return render(request, "collaboration_api.html")


def success_page(request):
    return render(request, "success_page.html")


def authView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})


@login_required
def profile(request):
    return render(request, "registration/profile.html")
