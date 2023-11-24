from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('sneakers/', views.ShowSneakers, name='sneakers'),
    path('electronics/', views.ShowElectronics, name='electronics'),
    path('addToCart/<int:pk>/', views.AddToCart, name='addToCart'),
    path('cart/', views.ShowCartPage, name='Cart'),
    path('addIcount/<int:pk>/', views.ShowCartPage, name='addIcount'),
    ]
