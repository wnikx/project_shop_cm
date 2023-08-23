from django.shortcuts import render
from .models import Product, Category


def main_page(request):
    return render(request, 'shop/main/main_page.html')


def list_categories(request):
    products_list = Category.objects.all()
    return render(request, 'shop/main/products.html',
                  {'products': products_list})


def category_products(request, category):
    category = Category.objects.filter(slug=category)
    products = Product.objects.filter(category=category.category_sid)
    return render(request, 'shop/main/category_products.html',
                  {'products': products,
                   'category': category})
