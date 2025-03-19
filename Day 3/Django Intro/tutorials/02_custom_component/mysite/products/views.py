from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Product

def index(*args, **kwargs):
    return HttpResponse("<h1>Hello, World!</h1>")

def about(request, *args, **kwargs):
    return render(request, "about.html", {})

def product(request, id, *args, **kwargs):
    product = Product.objects.get(id=id)
    context = product.__dict__
    print("Image path:", product.image.url if product.image else "No image")  # Debug line

    context["image"] = product.image.path
    return render(request, "product.html", context)
