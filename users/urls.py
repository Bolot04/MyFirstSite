from django.urls import path

from users.views import profile_view, register_view, login_view, logout_view

urlpatterns = [
    path('profile/', profile_view),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout')
]
