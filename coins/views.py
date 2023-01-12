from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required
from .models import Metal, Coins
from .forms import CoinsForm


def all_coins(request):
    """
    A view to show all coins
    """
    coins = Coins.objects.filter(quantity__gt=0)
    query = None
    eras = None
    metals = None
    sort = None
    direction = None

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

    if 'metal' in request.GET:
        metals = request.GET['metal'].split(',')
        coins = coins.filter(metal__name__in=metals)
        metals = Metal.objects.filter(name__in=metals)

    if 'sort' in request.GET:
        sortkey = request.GET['sort']
        sort = sortkey
        if sortkey == 'name':
            sortkey = 'lower_name'
            coins = coins.annotate(lower_name=Lower('name'))
        if sortkey == 'metal':
            sortkey = 'metal__name'
        if 'direction' in request.GET:
            direction = request.GET['direction']
            if direction == 'desc':
                sortkey = f'-{sortkey}'
        coins = coins.order_by(sortkey)

    current_sorting = f'{sort}_{direction}'

    context = {
        'coins': coins,
        'search_term': query,
        'current_metals': metals,
        'current_sorting': current_sorting,

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


@login_required
def add_coins(request):
    """
    Add a product to the store
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = CoinsForm(request.POST, request.FILES)
        if form.is_valid():
            coins = form.save()
            messages.success(request, 'Coins added successfully!')
            return redirect(reverse('coins_detail', args=[coins.id]))
        else:
            messages.error(request, 'Failed to add coins. Please ensure the form is valid.')
    else:
        form = CoinsForm()

    template = 'coins/add_coins.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def delete_coins(request, coins_id):
    """
    Delete a product from the store
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    coins = get_object_or_404(Coins, pk=coins_id)
    coins.delete()
    messages.success(request, 'Coins deleted!')
    return redirect(reverse('coins'))


@login_required
def edit_coins(request, coins_id):
    """
    Edit a product in the store
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    coins = get_object_or_404(Coins, pk=coins_id)
    if request.method == 'POST':
        form = CoinsForm(request.POST, request.FILES, instance=coins)
        if form.is_valid():
            form.save()
            messages.success(request, 'Coins successfully updated!')
            return redirect(reverse('coins_detail', args=[coins.id]))
        else:
            messages.error(request, 'Failed to update. Please ensure the form is valid.')
    else:
        form = CoinsForm(instance=coins)
        messages.info(request, f'You are editing {coins.name}')

    template = 'coins/edit_coins.html'
    context = {
        'form': form,
        'coins': coins,
    }

    return render(request, template, context)
