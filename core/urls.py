from django.urls import path
from core.views import home, test, login


urlpatterns = [
    path("", home, name="home"),
    path("test/", test, name="test"),
    path("login/", login, name="login"),
]