from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    """
    Class for contact admin model
    """
    list_display = (
        'email',
        'name',
        'buy_sell',
        'phone_nr',
    )


admin.site.register(Contact, ContactAdmin)
