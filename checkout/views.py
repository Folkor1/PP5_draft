from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Coins
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from bag.contexts import cart_contents

import stripe
import json
