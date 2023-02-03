from django import forms

from reservation_system.menu.models import Menu


class BootstrapFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_fields()

    def _init_bootstrap_fields(self):
        for (_, field) in self.fields.items():
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = ''
            field.widget.attrs['class'] += 'form-control'


class ProductForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'some-class',
                }
            )
        }


class EditProductForm(ProductForm):
    class Meta:
        model = Menu
        fields = ('name', 'type', 'description', 'price',)
        widgets = {
            'type': forms.TextInput(
                attrs={
                    'readonly': 'readonly',
                }
            )
        }