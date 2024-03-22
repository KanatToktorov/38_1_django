from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

import product
from product.models import Product, Category


def hello_view(request):
    if request.method == 'GET':
        return HttpResponse('Hello! It is my project')

# def main_page_view(request):
#     if request.method == 'GET':
#         return render(request, 'main.html')

def current_date_view(request):
    now = datetime.now()
    return HttpResponse(f"Current date: {now.strftime('%Y-%m-%d')}")

def goodbye_view(request):
    return HttpResponse('Goodbye user!')

def main_page_view(request):
    MOCK_DATA = [
        {
            'id': 1,
            'name': 'John',
            'age': 25
        },
        {
            'id': 2,
            'name': 'Jane',
            'age': 30
        },
        {
            'id': 3,
            'name': 'Bob',
            'age': 35
        }
    ]

    context = {'name': 'Kanat', 'mock_data': MOCK_DATA}
    if request.method == 'GET':
        return render(request, 'main.html', context=context)


def product_list_view(request):
    # 1. Достаем все посты из базы данных
    products = Product.objects.all()

    # 2. Передаем посты в контекст
    context = {'products': products}

    # 3. Отображаем шаблон
    return render(request, 'product/product_list.html', context)


def product_detail_view(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return render(request, 'errors/404.html')

    context = {'product': product}

    return render(request, 'product/product_detail.html', context)


def category_list_view(request):
    categories = Category.objects.all()
    context = {'product': product}
    return render(request, 'product/product_detail.html', context)