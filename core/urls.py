from django.urls import path
from core.views import home, login, registration, profile, logout


urlpatterns = [
    path("", home, name="home"),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("registration/", registration, name="registration"),
    path("profile/<int:pk>/", profile, name="profile"),
]