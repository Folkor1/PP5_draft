from django.contrib import admin
from .models import Metal, Coins


class CoinsAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'metal',
        'price',
        'quantity',
        'origin',
        'year',
        'condition',
        'era',
        'image',
        'id',
    )

    ordering = ('metal',)


class MetalAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Coins, CoinsAdmin)
admin.site.register(Metal, MetalAdmin)
