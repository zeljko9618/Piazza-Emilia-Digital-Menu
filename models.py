from django.db import models
from django.contrib.auth.models import User

TYPE = (
    ("beverage", "Beverage"),
    ("food", "Food")
)

MEAL_TYPES = (
    ("starters", "Starters"),
    ("salads", "Salads"),
    ("main_dishes", "Main Dishes"),
    ("desserts", "Desserts")
)

DRINK_TYPES = (
    ("coffee_drinks", "Coffee Drinks"),
    ("soft_drinks", "Soft Drinks"),
    ("alcoholic_drinks", "Alcoholic Drinks")
)

STATUS = (
    (0, "Unavailable"),
    (1, "Available")
)


# Form of our database
class Item(models.Model):
    item = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    type = models.CharField(max_length=100, choices=TYPE)
    meal_type = models.CharField(max_length=100, choices=MEAL_TYPES, null=True, blank=True)
    drink_type = models.CharField(max_length=100, choices=DRINK_TYPES, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.CharField(STATUS, max_length=100, default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item
