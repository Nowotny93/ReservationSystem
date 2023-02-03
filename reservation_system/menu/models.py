from django.contrib.auth import get_user_model
from django.db import models


UserModel = get_user_model()


class Menu(models.Model):
    TYPE_CHOICE_BEVERAGE = 'Beverage'
    TYPE_CHOICE_STARTER = 'Starter'
    TYPE_CHOICE_MAIN_DISH = 'Main Dish'
    TYPE_CHOICE_DESSERT = 'Dessert'

    TYPE_CHOICES = (
        (TYPE_CHOICE_BEVERAGE, 'Beverage'),
        (TYPE_CHOICE_STARTER, 'Starter'),
        (TYPE_CHOICE_MAIN_DISH, 'Main Dish'),
        (TYPE_CHOICE_DESSERT, 'Dessert'),
    )

    name = models.CharField(
        max_length=50,
    )

    type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES,
        null=True,
    )

    description = models.CharField(max_length=100)
    # image_url = models.URLField()

    price = models.FloatField()

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
   )

    def __str__(self):
        return f'{self.name}, {self.description} - {self.price} lv.'
