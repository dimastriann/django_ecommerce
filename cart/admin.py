from django.contrib import admin
from .models import Cart, CartItem


class CartItemInline(admin.TabularInline):
    model = CartItem


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ["cart_id", "user", "date_added"]
    inlines = [CartItemInline]
