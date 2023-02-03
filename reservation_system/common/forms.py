from collections import OrderedDict

from django import forms
from django.core.exceptions import ObjectDoesNotExist

from reservation_system.common.models import MakeOrder


# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('text',)
from reservation_system.inventory.fields import GroupedModelChoiceField
from reservation_system.menu.models import Menu


# def get_my_choices():
#     choices_list = []
#     for obj in Menu.objects.all():
#         choices_list.append(obj.name)
#     return choices_list

class MakeOrderForm(forms.ModelForm):
    # def __init__(self, name, *args, **kwargs):
    #     super(MakeOrderForm, self).__init__(*args, **kwargs)
    #     self.fields["name"] = forms.ChoiceField(choices=name)

    # def __init__(self, *args, **kwargs):
    #     super(MakeOrderForm, self).__init__(*args, **kwargs)
    #     self.fields['name'].choices = forms.ChoiceField(choices=get_my_choices())
    # product = GroupedModelChoiceField(
    #     queryset=Menu.objects.exclude(type=None),
    #     choices_groupby='type'
    # )

    class Meta:
        model = MakeOrder
        fields = ('product',)


    def __init__(self, *args, **kwargs):
        super(MakeOrderForm, self).__init__(*args, **kwargs)

        product_choices_dict = {'-': 'Chose a product'}
        for product in self.fields["product"].queryset.order_by("name"):
            choice_tuple = (product.pk, product.name)
            try:
                product_type = product.type
            except (AttributeError, ObjectDoesNotExist):
                product_type = False
            try:
                product_choices_dict[product_type].append(choice_tuple)
            except KeyError:
                product_choices_dict[product_type] = [choice_tuple]

        self.fields["product"].choices = product_choices_dict.items()
        self.fields['product'].widget.attrs['style'] = 'height: 40px'




