from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from reservation_system.core.views import BootStrapFormViewMixin
from reservation_system.menu.forms import EditProductForm
from reservation_system.menu.models import Menu


class MenuView(ListView):
    template_name = 'products/menu.html'
    model = Menu
    context_object_name = 'menus'


class AddProductView(LoginRequiredMixin, BootStrapFormViewMixin, CreateView):
    model = Menu
    fields = ('name', 'description', 'type', 'price')
    success_url = reverse_lazy('list menu')
    template_name = 'products/create_product.html'

    def form_valid(self, form):
        product = form.save(commit=False)
        product.user = self.request.user
        product.save()
        return super().form_valid(form)


# class EditProductView(LoginRequiredMixin, UpdateView):
#     model = Menu
#     template_name = 'products/edit_product.html'
#     form_class = EditProductForm
#     success_url = reverse_lazy('list menu')

def edit_product(request, pk):
    product = Menu.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('list menu')
    else:
        form = EditProductForm(instance=product)

    context = {
        'form': form,
        'product': product,
    }
    return render(request, 'products/edit_product.html', context)


class DeleteProductView(LoginRequiredMixin, DeleteView):
    template_name = 'products/delete_product.html'
    model = Menu
    success_url = reverse_lazy('list menu')
    context_object_name = 'product'
