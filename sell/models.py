from django.db import models


class Sell(models.Model):
    """
    Class for Sell model
    """

    email = models.EmailField(max_length=70, null=True)
    coin_name = models.CharField(max_length=50)
    description = models.TextField()
    metal = models.CharField(max_length=50)
    origin = models.CharField(max_length=50)
    condition = models.CharField(max_length=100)
    ask_price = models.DecimalField(max_digits=8, decimal_places=2)
    negotiable = models.BooleanField(default=False)
    image = models.ImageField(blank=False)

    def __str__(self):
        return self.coin_name

    @property
    def price_display(self):
        return "$%s" % self.ask_price

    class Meta:
        verbose_name_plural = 'Sell'
