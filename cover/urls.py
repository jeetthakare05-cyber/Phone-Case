from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    path('about/', views.about, name='about'),

    path('contact/', views.contact, name='contact'),

    path('suggestions/', views.suggestions, name='suggestions'),
     
    path("cart/", views.cart, name="cart"),

path("add-to-cart/<int:product_id>/", views.add_to_cart, name="add_to_cart"),

path('increase/<int:cart_id>/', views.increase_quantity, name='increase_quantity'),

path('decrease/<int:cart_id>/', views.decrease_quantity, name='decrease_quantity'),

path('remove/<int:cart_id>/', views.remove_from_cart, name='remove_from_cart'),

path('checkout/', views.checkout, name='checkout'),

path(
    "product/<int:product_id>/",
    views.product_detail,
    name="product_detail"
),
]

