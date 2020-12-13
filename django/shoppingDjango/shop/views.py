from django.shortcuts import render, get_object_or_404

from django.conf import settings
from cart.cart import Cart
from cart.forms import AddProductForm
from .models import *

def product_in_category(request, category_slug=None):
    current_category = None

    categories = Category.objects.all()

    products = Product.objects.filter(available_display=True)
    cart = Cart(request)

    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=current_category)

    context = {
        'current_category': current_category,
        'categories': categories,
        'products': products,
        'cart': cart,
    }
    return render(request, 'shop/list.html', context)


def product_detail(request, id, product_slug=None):
    product = get_object_or_404(Product, id=id, slug=product_slug)

    add_to_cart = AddProductForm(initial={'quantity': 1})

    context = {
        'product': product,
        'add_to_cart': add_to_cart,
    }
    return render(request, 'shop/detail.html', context)