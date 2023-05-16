from django.urls import path
from django.contrib.auth import views as auth_views
from main.views import catalog

from .views import RegisterView

urlpatterns = [
    path('', catalog, name='catalog'),
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]