from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.main, name='main'),
    path('register/', views.register, name='register'),
    path('login/', auth_view.LoginView.as_view(template_name='steamClone/Login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='steamClone/Main.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('cart/', views.cart, name='cart'),
    path('add/', views.add, name='add'),
    path('edit/', views.edit, name='edit'),
    path('delete/', views.delete, name='delete'),
]
