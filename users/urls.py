from django.urls import path

from users.views import profile_view, register_view, login_view, logout_view

urlpatterns = [
    path('profile/', profile_view),
    path('register/', register_view),
    path('login/', login_view),
    path('logout/', logout_view)
]
