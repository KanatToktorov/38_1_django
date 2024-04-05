from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.db.models import Q

import product
from product.models import Product, Category, Review, Tag
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
    search = request.GET.get('search')
    sort = request.GET.get('sort', 'created_at')
    tag = request.GET.get('tag')
    page = request.GET.get('page', 1)

    products = Product.objects.all()

    if search:
        products = products.filter(
            Q(title__icontains=search) | Q(content__icontains=search)
        )
        # products = products.filter(title__icontains=search) | products.filter(description__icontains=search)
        # icontains - case-insensitive search
        # contains - case-sensitive search

    if tag:
        products = products.filter(tags__id=tag)

    products = products.order_by(sort)

    limit = 3
    # posts = [post1, post2, post3, post4, post5, post6, post7, post8, post9, post10]
    # page = 1, limit = 3

    # formula:
    # start = (page - 1) * limit
    # end = page * limit

    start = (int(page) - 1) * limit
    end = int(page) * limit

    all_pages = len(products) / limit
    if round(all_pages) < all_pages:
        all_pages += 1
    all_pages = round(all_pages)

    tags = Tag.objects.all()
    context = {
        'products': products[start:end],
        'tags': tags,
        'all_pages': range(1, all_pages + 1)
    }

    return render(request, 'product/product_list.html', context)
# @login_required
# def product_list_view(request):
#     # 1. Достаем все продукты из базы данных
#     products = Product.objects.all().exclude(user=request.user)
#
#     # 2. Передаем продукты в контекст
#     context = {'products': products}
#
#     # 3. Отображаем шаблон
#     return render(request, 'product/product_list.html', context)


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


def product_change_view(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return render(request, 'errors/404.html')

    if request.method == 'GET':
        form = ProductForm2(instance=product)
        return render(request, 'product/product_change.html', {'form': form})
    if request.method == 'POST':
        form = ProductForm2(request.POST, request.FILES, instance=product)
        if not form.is_valid():
            return render(request, 'product/product_change.html', {'form': form})

        form.save()
        return redirect('product_list')


def product_delete_view(request, product_id):
    try:
        post = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return render(request, 'errors/404.html')

    post.delete()
    return redirect('product_list')