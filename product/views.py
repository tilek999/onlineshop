from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required, user_passes_test
from product.models import Product, Category 
from product.forms import ProductForm


def products(request):
    context = {}
    if "query" in request.GET:
        word = request.GET.get("query")
        context["products"] = Product.objects.filter(
            Q(avialable=True),
            Q(name__contains=word) |
            Q(description__contains=word) |
            Q(category__name__contains=word) |
            Q(price__contains=word)  
        )
    else:
        context["products"] = Product.objects.filter(avialable=True)
    return render(request, "product/products.html", context)


def product(request, id):
    context = {}
    context["product"] = Product.objects.get(id=id)
    return render(request, "product/product.html", context)


@login_required(login_url="login")
def product_create(request):
    context = {}
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            context["products"] = Product.objects.filter(avialable=True)
            context["message"] = "Товар был успешно добавлен"
            return render(request, "product/products.html", context)
    
    context["form"] = ProductForm()

    return render(
        request,
        "product/form.html",
        context
    )


def product_edit(request, id):
    product = Product.objects.get(id=id)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product", id=product.id)
    
    context = {}
    context["form"] = ProductForm(instance=product)

    return render(
        request,
        "product/form.html",
        context
    )


@login_required(login_url='/login/')
def product_delete(request, id):
    product = Product.objects.get(id=id)
    context = {}

    if product.user != request.user:
        context["message"] = "У вас нет доступа!"
    else:
        product.deleted = True
        product.save()
        context["message"] = "Товар был удалён"
    
    context["type"] = "danger"
    return render(request, "core/message.html", context)