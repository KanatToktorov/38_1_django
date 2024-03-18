'''
admin.py - это файл, в котором мы будем регистрировать наши модели для административного интерфейса.
'''

from django.contrib import admin

from product.models import Product


admin.site.register(Product)
