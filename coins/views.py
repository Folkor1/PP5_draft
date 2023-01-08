from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Metal, Coins


def all_coins(request):
    """
    A view to show all coins
    """
    coins = Coins.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('coins'))

            queries = (
                Q(name__icontains=query) |
                Q(description__icontains=query) |
                Q(origin__icontains=query) |
                Q(condition__icontains=query) |
                Q(year__icontains=query)
                )
            coins = coins.filter(queries)

    if 'era' in request.GET:
        eras = request.GET['era'].split(',')
        coins = coins.filter(era__in=eras)
        eras = Coins.objects.filter(name__in=eras)

    if 'condition' in request.GET:
        conditions = request.GET['condition'].split(',')
        coins = coins.filter(condition__in=conditions)
        conditions = Coins.objects.filter(name__in=conditions)

    if 'metal' in request.GET:
        metals = request.GET['metal'].split(',')
        coins = coins.filter(metal__name__in=metals)
        metals = Metal.objects.filter(name__in=metals)

    context = {
        'coins': coins,
        'search_term': query,
    }

    return render(request, 'coins/coins.html', context)


def coins_detail(request, coins_id):
    """
    A view to show individual coin details
    """

    coins = get_object_or_404(Coins, pk=coins_id)

    context = {
        'coins': coins,
    }

    return render(request, 'coins/coins_detail.html', context)
