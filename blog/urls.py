from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from post.views import hello_view, \
    main_page_view, goodbye_view, current_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page_view),
    path('hello/', hello_view),
    path('current_date/', current_view),
    path('goodbye/', goodbye_view),
    path('', include('post.urls')), # include - для связки других urls
    path('', include('users.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
