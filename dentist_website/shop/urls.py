from django.urls import path 
from .import views

urlpatterns = [path('', views.shop),
    path ('main.html', views.shop),
    path ('cart.html', views.cart),
    path ('checkout.html', views.checkout),
    path ('shop.html', views.shop),
    
]