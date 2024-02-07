from django.urls import path

from post.views import products_page_view, products_list_view, product_detail_view, categories_view, \
    product_create_view, category_create_view

urlpatterns = [
    path('', products_page_view),
    path('product/', products_list_view),
    path('product/<int:product_id>/', product_detail_view),
    path('category/', categories_view),
    path('products/create/', product_create_view),
    path('categories/create/', category_create_view),
]