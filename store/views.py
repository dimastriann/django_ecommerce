from django.shortcuts import get_object_or_404, render
from .models import Category, Product

from django.db.models import Q


def home(request):
    products = Product.objects.filter(is_active=True).order_by("-created")[:8]
    return render(request, "home.html", {"products": products})


def product_all(request):
    products = Product.objects.filter(is_active=True)
    query = request.GET.get("q")
    if query:
        products = products.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
    return render(request, "store/product_list.html", {"products": products})


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(
        request, "store/product_list.html", {"category": category, "products": products}
    )


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, "store/product_detail.html", {"product": product})
