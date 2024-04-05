from django.urls import path

from product.views import (hello_view, main_page_view,
                           current_date_view, goodbye_view,
                           product_list_view, product_detail_view,
                           category_list_view, product_create_view,
                           product_change_view, product_delete_view,)


urlpatterns = [
    path('', main_page_view),
    path('hello/', hello_view),
    path('current_date/', current_date_view),
    path('goodbye/', goodbye_view),
    path('products/', product_list_view, name='product_list'),
    path('products/<int:product_id>/', product_detail_view, name='product_detail'),
    path('categories/', category_list_view, name='category_list'),
    path('products/create/', product_create_view, name='product_create'),
    path('products/<int:post_id>/update/', product_change_view, name='post_edit'),
    path('products/<int:post_id>/delete/', product_delete_view, name='post_delete'),
]

