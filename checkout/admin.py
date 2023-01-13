from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """
    Model for all products in the order
    """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """
    Model for all orders
    """
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_nr', 'date',
                       'grand_total', 'original_cart',
                       'stripe_pid')

    fields = ('order_nr', 'date', 'full_name',
              'email', 'phone_nr', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'grand_total',
              'original_cart', 'stripe_pid')

    list_display = ('order_nr', 'date', 'full_name',
                    'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
