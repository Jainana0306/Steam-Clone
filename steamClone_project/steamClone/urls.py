from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.main, name='main'),
    path('register/', views.register, name='register'),
    path('login/', auth_view.LoginView.as_view(template_name='steamClone/Login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='steamClone/Login.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('cart/', views.cart, name='cart'),
    path('add/', views.add, name='add'),
    path('add/<int:id>', views.add, name='edit'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('gameList/', views.gameList, name='list'),
    path('genreAdd/', views.genreAdd, name='genreAdd'),
    path('genreDelete/<int:id>', views.genreDelete, name='genreDelete'),
    path('detail/<int:id>', views.detail, name='detail'),
]
