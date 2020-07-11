from django.shortcuts import render
from product.models import Product, Category 
from product.forms import ProductForm

# Create your views here.
def products(request):
    context = {}
    context["products"] = Product.objects.filter(avialable=True)
    return render(request, "product/products.html", context)


def product(request, id):
    context = {}
    context["product"] = Product.objects.get(id=id)
    return render(request, "product/product.html", context)


def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(products)
    
    context = {}
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