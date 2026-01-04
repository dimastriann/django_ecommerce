import os
import django

from django.test import Client
from store.models import Category, Product

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()


def verify():
    # Setup
    cat, _ = Category.objects.get_or_create(name="Test Cat", slug="test-cat")
    prod, _ = Product.objects.get_or_create(
        category=cat,
        title="Test Product",
        slug="test-product",
        defaults={"price": 10.00, "in_stock": True},
    )

    c = Client()

    # Test List
    response = c.get("/")
    if response.status_code == 200 and "Test Product" in str(response.content):
        print("Product List: OK")
    else:
        print(f"Product List: FAILED ({response.status_code})")

    # Test Detail
    response = c.get(prod.get_absolute_url())
    if response.status_code == 200 and "Test Product" in str(response.content):
        print("Product Detail: OK")
    else:
        print(f"Product Detail: FAILED ({response.status_code})")


if __name__ == "__main__":
    verify()
