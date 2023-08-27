from django.shortcuts import render
from .models import Product, Category


def main_page(request):
    return render(request, 'shop/main/main_page.html')


def list_categories(request):
    products_list = Category.objects.all()
    return render(request, 'shop/main/products.html',
                  {'products': products_list})


def category_products(request, category):
    category = Category.objects.get(slug=category)
    print(category)
    products = Product.objects.filter(category=category.id)
    print(products)
    return render(request, 'shop/main/category_products.html',
                  {'products': products,
                   'category': category})


def info_product(request, category, product):
    print('Тут')
    product = Product.objects.get(slug=product)
    return render(request, 'shop/main/info_product.html',
                  {'product': product})
