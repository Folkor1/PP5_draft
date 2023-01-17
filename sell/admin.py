from django.contrib import admin
from .models import Sell


class SellAdmin(admin.ModelAdmin):
    """
    Class for sell admin model
    """
    list_display = (
        'email',
        'coin_name',
        'metal',
        'ask_price',
        'negotiable',
        'origin',
        'condition',
        'image',
    )

    ordering = ('ask_price',)


admin.site.register(Sell, SellAdmin)
