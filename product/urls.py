from django.urls import path

from product.views import (hello_view, main_page_view,
                           current_date_view, goodbye_view,
                           product_list_view, product_detail_view,
                           category_list_view, product_create_view,
                           product_change_view, product_delete_view,
                           HelloView, ProductListView, ProductDetailView,
                           ProductCreateView, ProductUpdateView,
                           CurrentDateView, GoodbyeView, CategoryListView)


urlpatterns = [
    path('', main_page_view),

    path('hello/', hello_view),
    path('hello2/', HelloView.as_view(), name='hello2'),

    path('current_date/', current_date_view),
    path('current_date2/', CurrentDateView.as_view(), name='current_date2'),

    path('goodbye/', goodbye_view),
    path('goodbye2/', GoodbyeView.as_view(), name='goodbye2'),

    path('products/', product_list_view, name='product_list'),
    path('products2/', ProductListView.as_view(), name='product_list2'),

    path('products/<int:product_id>/', product_detail_view, name='product_detail'),
    path('products2/<int:product_id>/', ProductDetailView.as_view(), name='product_detail2'),

    path('categories/', category_list_view, name='category_list'),
    path('categories2/', CategoryListView.as_view(), name='category_list2'),

    path('products/create/', product_create_view, name='product_create'),
    path('products2/create/', ProductCreateView.as_view(), name='product_create2'),

    path('products/<int:product_id>/update/', product_change_view, name='product_edit'),
    path('products2/<int:product_id>/update/', ProductUpdateView.as_view(), name='product_edit2'),

    path('products/<int:product_id>/delete/', product_delete_view, name='post_delete'),
]

