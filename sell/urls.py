from django.urls import path
from . import views

urlpatterns = [
    path('', views.sell_coins, name='sell_coins'),
]
