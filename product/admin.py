'''
admin.py - это файл, в котором мы будем регистрировать наши модели для административного интерфейса.
'''

from django.contrib import admin
from product.models import Product, Review, Tag, Category
from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest

# admin.site.register(Product)
# admin.site.register(Review)
# admin.site.register(Tag)
# admin.site.register(Category)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('title', 'content')
    readonly_fields = ('created_at', 'updated_at', 'id')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
        pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
        pass

def save_model(self, request, obj, form, change):
    obj.title = obj.title.capitalize()
    super().save_model(request, obj, form, change)

    # fields = ('id', 'title', 'description', 'price', 'tags', 'created_at', 'updated_at')

    # fieldsets = (
    #     ("General", {
    #         'fields': ('title', 'description', 'tags')
    #     }),
    #     ('Readonly Fields', {
    #         'fields': ('id', 'price', 'created_at', 'updated_at'),
    #         # 'classes': ('collapse',)
    #     }),
    # )



    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #     return qs.filter(price>5)

    # def has_add_permission(self, request):
    #     if Product.objects.count() >= 10:
    #         return False
    #     return True

    # def has_change_permission(self, request, obj=None):
    #     return False

    # def has_delete_permission(self, request, obj=None):
    #     return False



