from django.shortcuts import render
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
