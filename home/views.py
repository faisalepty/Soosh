from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from .models import Product, Category, Subcategory, Cart

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
    allShoes = Product.objects.filter(subcategory__maincategory__name='Sneakers')
    categories = Subcategory.objects.filter(maincategory__name='Sneakers')
    # apply filters if exist
    q = request.GET.get('q') or request.GET.get('r') if request.GET.get('q') or request.GET.get('r') != None else ''
    s = 's'
    FilteredShoes = Product.objects.filter(
        Q(name__icontains=q, subcategory__maincategory__name='Sneakers') |
        Q(variation__color__icontains=q, subcategory__maincategory__name='Sneakers')
    )
    if FilteredShoes:
        allShoes = FilteredShoes
    else:
        allShoes = Product.objects.filter(subcategory__maincategory__name='Sneakers')

    context = {'products': allShoes, 'categories': categories, 'FilteredShoes': FilteredShoes, 'q': q, 's': s}
    return render(request, 'sneakers.html', context)


def ShowElectronics(request):
    allElectronics = Product.objects.filter(subcategory__maincategory__name='Electronics')
    categories = Subcategory.objects.filter(maincategory__name='Electronics')

    # apply filters if exist
    q = request.GET.get('q') or request.GET.get('r') if request.GET.get('q') or request.GET.get('r') != None else ''
    e = 'e'
    Filteredelectronics = Product.objects.filter(
        Q(name__icontains=q, subcategory__maincategory__name='Electronics') |
        Q(variation__color__icontains=q, subcategory__maincategory__name='Electronics')
    )
    if Filteredelectronics:
        allElectronics = Filteredelectronics
    else:
        allElectronics = Product.objects.filter(subcategory__maincategory__name='Electronics')
    filter_multiples = []
    for i in allElectronics:
        if i not in filter_multiples:
            filter_multiples.append(i)


    context = {'products': filter_multiples, 'categories': categories, 'Filteredelectronics': Filteredelectronics, 'q': q, 'e': e}
    return render(request, 'electronics.html', context)

def AddToCart(request, pk):
    product = Product.objects.get(id=pk)
    cartItems = Cart.objects.all()
    cartItemsList = [cartItem.product.id for cartItem in cartItems]
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        if pk not in cartItemsList:
        
            newCartItem = Cart(product=product, user=request.user)
            newCartItem.save()
            return JsonResponse({'data': cartItemsList})
        else:
            return JsonResponse({'error': 'Product is already in the cart'}, status=400)


