# """
# URL configuration for firtPrj project.

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/5.0/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import path
# from pages.views import home_view,about_view
# from .views import (product_detail_view, product_create_view,product_delete_view, product_list_view, product_update_view
# )
# app_name = 'products'
# urlpatterns = [
#     path('', product_list_view, name='product-list'),
#     path('create/', product_create_view, name='product-list'),
#     path('<int:id>/', product_detail_view, name='product-detail'),
#     path('<int:id>/update/', product_update_view, name='product-update'),
#     path('<int:id>/delete/', product_delete_view, name='product-delete'),
# ]  


from django.contrib import admin
from django.urls import include, path

from pages.views import home_view,about_view


urlpatterns = [
    path('products/', include('products.urls')),
    path('', home_view, name='home'),
    path('about/<int:id>/', about_view, name='product-detail'),

    path('admin/', admin.site.urls),
]

