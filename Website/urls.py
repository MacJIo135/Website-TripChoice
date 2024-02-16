from django.urls import path, include
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("signup/", authView, name="authView"),
    path("about-site/", about_site, name="about_site"),
    path("agents/", agents, name="agents"),
    path("collaboration-api/", collaboration_api, name="collaboration_api"),
    path("collaboration-api/success/", success_page, name="success_page"),
    path("accounts/", include("django.contrib.auth.urls"))
]