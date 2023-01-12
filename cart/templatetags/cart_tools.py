from django import template


register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, coin_quantity):
    return price * coin_quantity
