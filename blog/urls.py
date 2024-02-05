from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from post.views import hello_view, \
    main_page_view, goodbye_view, current_view, products_page_view, \
    products_list_view, product_detail_view, categories_view, product_create_view, category_create_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page_view),
    path('hello/', hello_view),
    path('current_date/', current_view),
    path('goodbye/', goodbye_view),
    path('', products_page_view),
    path('product/', products_list_view),
    path('product/<int:product_id>/', product_detail_view),
    path('category/', categories_view),
    path('products/create/', product_create_view),
    path('categories/create/', category_create_view),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
