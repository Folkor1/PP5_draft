from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import Sell
from .forms import SellForm


def sell_coins(request):
    """
    Add coins to sell
    """

    if request.method == 'POST':
        form = SellForm(request.POST, request.FILES)
        if form.is_valid():
            sell = form.save()
            messages.success(request, 'Thanks! We will review the offer and get in touch with you.')
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Failed to ')
    else:
        form = SellForm()

    template = 'sell/sell.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
