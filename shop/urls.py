from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('category/<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('product/<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
path('profile/', views.profile_view, name='profile'),

path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
path('cart/', views.view_cart, name='view_cart'),
]
