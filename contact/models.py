from django.db import models

BUY_SELL_CHOICES = (
    ("buyer", "Buyer"),
    ("seller", "Seller"),
)


class Contact(models.Model):
    """
    Class for Contact model
    """
    email = models.EmailField(max_length=70)
    name = models.CharField(max_length=50)
    buy_sell = models.CharField(max_length=20, choices=BUY_SELL_CHOICES, default=None)
    phone_nr = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Contacts'
