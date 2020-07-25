from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from core.forms import ChangePasswordForm
from product.models import Product


@login_required(login_url="/login/")
def profile(request, pk):
    context = {}
    context["user"] = User.objects.get(id=pk)
    context["products"] = Product.objects.filter(user=context["user"])
    context["password_change_form"] = ChangePasswordForm()
    return render(request, "core/profile.html", context)