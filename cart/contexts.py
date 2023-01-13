from django.conf import settings
from django.shortcuts import get_object_or_404
from coins.models import Coins


def cart_contents(request):

    cart_items = []
    total = 0
    coins_count = 0
    cart = request.session.get('cart', {})

    for item_id, item_data in cart.items():
        if isinstance(item_data, int):
            coins = get_object_or_404(Coins, pk=item_id)
            unique = coins.quantity
            total += item_data * coins.price
            coins_count += item_data
            cart_items.append({
                'item_id': item_id,
                'coin_quantity': item_data,
                'coins': coins,
                'unique': unique,
            })
        else:
            coins = get_object_or_404(Coins, pk=item_id)
            for coin_quantity in item_data.items():
                total += coin_quantity * coins.price
                coins_count += coin_quantity
                cart_items.append({
                    'item_id': item_id,
                    'coin_quantity': coin_quantity,
                    'coins': coins,
                })

    grand_total = total

    context = {
        'cart_items': cart_items,
        'total': total,
        'coins_count': coins_count,
        'grand_total': grand_total,
    }

    return context
