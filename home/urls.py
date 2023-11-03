from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('sneakers/', views.ShowSneakers, name='sneakers'),
    path('electronics/', views.ShowElectronics, name='electronics'),
]