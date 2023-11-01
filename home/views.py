from django.shortcuts import render
from .models import Product

# Create your views here.

def Home(request):
    AllProducts = Product.objects.all().order_by('?')
    context = {
        'products': AllProducts
    }
    return render(request, 'index.html', context)
