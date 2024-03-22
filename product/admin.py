'''
admin.py - это файл, в котором мы будем регистрировать наши модели для административного интерфейса.
'''

from django.contrib import admin

from product.models import Product, Review, Tag, Category


admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Tag)
admin.site.register(Category)


