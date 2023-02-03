from django.contrib.auth import get_user_model
from django.db import models

from reservation_system.inventory.models import Table
from reservation_system.menu.models import Menu

UserModel = get_user_model()


# class Comment(models.Model):
#
#     text = models.TextField()
#     comment = models.ForeignKey(Table, on_delete=models.CASCADE, null=True)
#     user = models.ForeignKey(
#         UserModel,
#         on_delete=models.CASCADE,
#     )


class  MakeOrder(models.Model):
    # choices = tuple(Menu.objects.values_list('name', 'name'))
    # name = models.CharField(
    #     max_length=15,
    #     choices=choices,
    #     null=True,
    # )
    order = models.ForeignKey(Table, on_delete=models.CASCADE, null=True)

    product = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True)

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        null=True
    )