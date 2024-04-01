from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required

import product
from product.models import Product, Category, Review
from product.forms import ProductForm2, ReviewForm



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

@login_required
def product_list_view(request):
    # 1. Достаем все продукты из базы данных
    products = Product.objects.all().exclude(user=request.user)

    # 2. Передаем продукты в контекст
    context = {'products': products}

    # 3. Отображаем шаблон
    return render(request, 'product/product_list.html', context)


def product_detail_view(request, product_id):
    if request.method == 'GET':
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return render(request, 'errors/404.html')

        context = {'product': product, 'form': ReviewForm}

        return render(request, 'product/product_detail.html', context)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            Review.objects.create(product_id=product_id, **form.cleaned_data)
            return redirect(f'/products/{product_id}/')
        context = {
            'form': form,
        }
        return render(request, 'products/product_detail.html', context)


def category_list_view(request):
    categories = Category.objects.all()
    return render(request, 'categories/category_list.html', {'categories': categories})

@login_required(login_url='/auth/login')
def product_create_view(request):
    if request.method == 'GET':
        form = ProductForm2()
        return render(request, 'product/product_create.html', {'form': form})

    if request.method == 'POST':
        form = ProductForm2(request.POST, request.FILES)
        # form.add_error('content', 'Текст не должен содержать слово Python!')

        if not form.is_valid():
            return render(request, 'product/product_create.html', {'form': form})

        title = form.cleaned_data.get('title')
        description = form.cleaned_data.get('description')
        image = form.cleaned_data.get('image')
        price = form.cleaned_data.get('price')
        tags = form.cleaned_data.get('tags')

        product = Product.objects.create(
            title=title,
            description=description,
            image=image,
            price=price,
            user=request.user
        )

        product.tags.set(tags)
        # product.tags.add(1)
        product.save()

        return redirect('product_list')


