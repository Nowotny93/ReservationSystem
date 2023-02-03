from django.contrib.auth import get_user_model
from django.db import models

from reservation_system.menu.models import Menu

UserModel = get_user_model()


class Table(models.Model):
    TYPE_CHOICE_SMALL = 'Small'
    TYPE_CHOICE_MEDIUM = 'Medium'
    TYPE_CHOICE_BIG = 'Big'

    TYPE_CHOICES = (
        (TYPE_CHOICE_SMALL, 'Small'),
        (TYPE_CHOICE_MEDIUM, 'Medium'),
        (TYPE_CHOICE_BIG, 'Big'),
    )

    type = models.CharField(
        max_length=6,
        choices=TYPE_CHOICES,
        null=True,
    )

    name = models.CharField(
        max_length=9,
    )
    description = models.CharField(max_length=100)
    # image_url = models.URLField()
    # image = models.ImageField(
    #     upload_to='pets',
    # )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.description}, {self.type}'












