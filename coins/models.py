from django.db import models


class Metal(models.Model):
    """
    Class for Metal model
    """
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

    class Meta:
        verbose_name_plural = 'Metals'


CONDITION_CHOICES = (
    ("uncirculated", "Uncirculated"),
    ("fine", "Fine"),
    ("good", "Good"),
    ("fair", "Fair"),
)

ERA_CHOICES = (
    ("ancient", "Ancient"),
    ("medium", "Medium"),
    ("modern", "Modern"),
)


class Coins(models.Model):
    """
    Class for Coins model
    """
    metal = models.ForeignKey('Metal', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    origin = models.CharField(max_length=254)
    year = models.CharField(max_length=20)
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, default=None)
    era = models.CharField(max_length=20, choices=ERA_CHOICES, default=None)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Coins'
