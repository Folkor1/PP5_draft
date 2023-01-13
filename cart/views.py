from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from coins.models import Coins


def view_cart(request):
    """
    A view that renders the cart contents
    """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """
    Add coins to the cart
    """

    coins = get_object_or_404(Coins, pk=item_id)
    unique = Coins.objects.filter(quantity=1).values_list('id', flat=True)
    coin_quantity = int(request.POST.get('coin_quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        if int(item_id) in unique:
            cart[item_id] = 1
            messages.info(request, f'Coin {coins.name} already added to cart')
        else:
            cart[item_id] += coin_quantity
            messages.success(request, f'Updated quantity of coin {coins.name} in cart')
    else:
        cart[item_id] = coin_quantity
        messages.success(request, f'Coin {coins.name} added to cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """
    Adjust the quantity of coins in the cart
    """

    coins = get_object_or_404(Coins, pk=item_id)
    coin_quantity = int(request.POST.get('coin_quantity'))
    cart = request.session.get('cart', {})

    if coin_quantity > 0:
        cart[item_id] = coin_quantity
        messages.success(request, f'Updated {coins.name} quantity to {cart[item_id]}')
    else:
        cart.pop(item_id)
        messages.success(request, f'Removed {coins.name} from the cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """
    Remove the coin from the cart
    """

    try:
        coins = get_object_or_404(Coins, pk=item_id)
        cart = request.session.get('cart', {})

        cart.pop(item_id)
        messages.success(request, f'Removed {coins.name} from the cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
