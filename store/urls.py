from django.urls import path, include
from . import views

urlpatterns = [
    
    path('store/',views.store,name="store"),
    path('cart/',views.cart,name="cart"),
    path('checkout/',views.checkout,name="checkout"),
    
]