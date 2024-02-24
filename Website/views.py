from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .forms import AvatarForm
from .models import *


# Create your views here.
def home(request):
    return render(request, "home.html", {})


def about_site(request):
    return render(request, "about_site.html")


def agencies(request):
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
            return redirect('/profile/')

    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})


@login_required
def profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            print(f"Form is valid: {form.cleaned_data}")
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            print(f"User: {user_profile}")
            user_profile.save()
            return redirect('profile')

    else:
        form = AvatarForm(instance=user_profile)

    return render(request, "registration/profile.html", {"form": form, "user_profile": user_profile})


