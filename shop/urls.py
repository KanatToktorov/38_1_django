"""
URL configuration for shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from product.views import (hello_view, main_page_view,
                           current_date_view, goodbye_view, product_list_view)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page_view),
    path('hello/', hello_view),
    path('current_date/', current_date_view),
    path('goodbye/', goodbye_view),
    path('products/', product_list_view, name='product_list')
]
