from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DeleteView, DetailView

from reservation_system.common.forms import MakeOrderForm
from reservation_system.common.models import MakeOrder

from reservation_system.core.views import BootStrapFormViewMixin, PostOnlyView

from reservation_system.inventory.models import Table
from reservation_system.menu.models import Menu

from django.core.cache import cache


class TablesView(ListView):
    # counter = 0
    template_name = 'tables/list_tables.html'
    model = Table
    context_object_name = 'tables'

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)

        # table_bills = self.request.session.get('table_bills')
        data = cache.get('my_key')
        context['total_profit'] = data
        return context


class AddTableView(LoginRequiredMixin, BootStrapFormViewMixin, CreateView):
    model = Table
    fields = ('name', 'description', 'type')
    success_url = reverse_lazy('list tables')
    template_name = 'tables/create_table.html'

    def form_valid(self, form):
        table = form.save(commit=False)
        table.user = self.request.user
        table.save()
        return super().form_valid(form)


class DeleteTableView(LoginRequiredMixin, DeleteView):
    template_name = 'tables/delete_table.html'
    model = Table
    success_url = reverse_lazy('list tables')


def TableDetailsView(request, pk):
    table = Table.objects.get(pk=pk)
    menu = Menu.objects.all()

    profit = 0

    for order in table.makeorder_set.all():
        for product in menu:
            if order.product == product:
                profit += product.price

    context = {
        'table': table,
        'make_order_form': MakeOrderForm(),
        'orders': table.makeorder_set.all(),
        'menu': menu,
        'profit': profit,
    }

    return render(request, 'tables/table_details.html', context)


def make_order(request, pk):
    order = Table.objects.get(pk=pk)
    form = MakeOrderForm(request.POST)

    if form.is_valid():
        ordering = MakeOrder(
            product=form.cleaned_data['product'],
            order=order,
        )
        ordering.save()
    return redirect('table details', order.id)


class DeleteOrderView(LoginRequiredMixin, DeleteView):
    template_name = 'tables/delete_order.html'
    model = MakeOrder
    success_url = reverse_lazy('list tables')
    context_object_name = 'order'

    #
    # def get_success_url(self):
    #     url = reverse_lazy('table details', kwargs={'pk': self.object.id})
    #     return url


def delete_all_orders(request, pk):
    table = Table.objects.get(pk=pk)
    orders = table.makeorder_set.all()

    table_bills = 0
    all_orders = [str(x.product) for x in table.makeorder_set.all()]


    for o in all_orders:
        table_bills += float(o.split()[-2])

    if request.method == 'POST':
        orders.delete()
        cache.set('my_key', table_bills)
        # request.session['table_bills'] = table_bills
        return redirect('list tables')
    else:
        context = {
            'orders': all_orders,
            'profitTable': table_bills
        }
        return render(request, 'tables/delete_all_orders.html', context)




