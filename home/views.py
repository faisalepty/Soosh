from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from .models import Product, Category, Subcategory, Cart, Variation

# Create your views here.

def CartItemsCount(request):
    CartCount = Cart.objects.filter(user=request.user).count()
    return CartCount

def Home(request):
    # get all products
    AllProducts = Product.objects.all().order_by('?')
    # count items in the cart
    cartcount = CartItemsCount(request) or 0
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
        'cartcount': cartcount,
    }
    return render(request, 'home.html', context)

def ShowSneakers(request):
    allShoes = Product.objects.filter(subcategory__maincategory__name='Sneakers')
    categories = Subcategory.objects.filter(maincategory__name='Sneakers')
    variations = Variation.objects.filter(product__subcategory__maincategory__name='Sneakers').distinct()
    sizeVariations = [int(variation.size) for variation in variations]
    cartcount = CartItemsCount(request) or 0

    # apply filters if exist
    q = request.GET.get('q') or request.GET.get('r') if request.GET.get('q') or request.GET.get('r') != None else ''
    s = 's'
    FilteredShoes = Product.objects.filter(
        Q(name__icontains=q, subcategory__maincategory__name='Sneakers') |
        Q(variation__color__icontains=q, subcategory__maincategory__name='Sneakers')
    )
    if FilteredShoes:
        allShoes = FilteredShoes
        variations = variations.filter(Q(product__subcategory__brand_subcat__icontains=q) | Q(color__icontains=q))
        sizeVariations = [int(variation.size) for variation in variations]
    else:
        allShoes = Product.objects.filter(subcategory__maincategory__name='Sneakers')

    context = {'products': allShoes,
                'categories': categories,
                  'FilteredShoes': FilteredShoes,
                  'sizeVariations': sizeVariations,
                  'cartcount': cartcount,
                'q': q, 's': s}
    return render(request, 'sneakers.html', context)


def ShowElectronics(request):
    allElectronics = Product.objects.filter(subcategory__maincategory__name='Electronics')
    categories = Subcategory.objects.filter(maincategory__name='Electronics')
    cartcount = CartItemsCount(request) or 0
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


    context = {'products': filter_multiples,
                'categories': categories,
                  'Filteredelectronics': Filteredelectronics,
                  'cartcount': cartcount,
                    'q': q, 'e': e}
    return render(request, 'electronics.html', context)

def ShowCartPage(request, pk=None):
    if pk:
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            quantity = request.GET.get('quantity')
            product = Product.objects.get(id=pk)
            cartItem = Cart.objects.get(product=product)
            cartItem.quantity = int(quantity)
            cartItem.save()
            CartItems = Cart.objects.filter(user=request.user)    
            grandTotal = 0
            for item in CartItems:
                x = item.Total()
                grandTotal += x
            ucartItem = Cart.objects.get(product=product)
            fucartItem = {'quantity':ucartItem.quantity,
                           'total':ucartItem.Total(),
                           'grandTotal': grandTotal}
            return JsonResponse({'ucartItem': fucartItem})
    CartItems = Cart.objects.filter(user=request.user)    
    grandTotal = 0
    for item in CartItems:
        grandTotal += item.Total() 
    
    context = {'CartItems': CartItems, 'grandTotal': grandTotal}
    return render(request, 'cart.html', context)

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


