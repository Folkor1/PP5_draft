from django.shortcuts import render, get_object_or_404
from .models import Metal, Coins


def all_coins(request):
    """
    A view to show all coins
    """
    coins = Coins.objects.all()

    context = {
        'coins': coins,
    }

    return render(request, 'coins/coins.html', context)


def coins_detail(request, coins_id):
    """ A view to show individual coins details """

    coins = get_object_or_404(Coins, pk=coins_id)

    context = {
        'coins': coins,
    }

    return render(request, 'coins/coins_detail.html', context)
