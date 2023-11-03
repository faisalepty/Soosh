from django.shortcuts import render
from django.db.models import Q
from .models import Product

# Create your views here.

def Home(request):
    # get all products
    AllProducts = Product.objects.all().order_by('?')
    # apply filters if exist
    q = request.GET.get('q') or request.GET.get('r') if request.GET.get('q') or request.GET.get('r') != None else ''
    Productsfilters = Product.objects.filter(
        Q(name__icontains=q)
        ).order_by('?')
    if Productsfilters:
        AllProducts = Productsfilters
    else:
        AllProducts = Product.objects.all().order_by('?')

    context = {
        'products': AllProducts,
    }
    return render(request, 'home.html', context)

def ShowSneakers(request):
    allShoes = Product.objects.filter(subcategory__maincategory__name='Sneakers').distinct()

    # apply filters if exist
    q = request.GET.get('q') or request.GET.get('r') if request.GET.get('q') or request.GET.get('r') != None else ''

    FilteredShoes = Product.objects.filter(
        Q(name__icontains=q, subcategory__maincategory__name='Sneakers') |
        Q(variation__color__icontains=q, subcategory__maincategory__name='Sneakers')
    )
    if FilteredShoes:
        allShoes = FilteredShoes
    else:
        allShoes = Product.objects.filter(subcategory__maincategory__name='Sneakers')

    context = {'products': allShoes}
    return render(request, 'products.html', context)


def ShowElectronics(request):
    allElectronics = Product.objects.filter(subcategory__maincategory__name='Electronics')

   
    context = {'products': allElectronics}
    return render(request, 'products.html', context)


