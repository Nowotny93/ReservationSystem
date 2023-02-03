from django.urls import path
from . import views
from .views import TablesView, AddTableView, DeleteTableView, TableDetailsView, make_order, \
    delete_all_orders, DeleteOrderView

urlpatterns = [
    path('', TablesView.as_view(), name='list tables'),
    path('add/', AddTableView.as_view(), name='add table'),
    path('delete/<int:pk>', DeleteTableView.as_view(), name='delete table'),
    path('details/<int:pk>', TableDetailsView, name='table details'),
    #path('comment/<int:pk>', CommentTableView.as_view(), name='comment table'),
    path('makeorder/<int:pk>', make_order, name='make order'),
    path('deleteorder/<int:pk>', DeleteOrderView.as_view(), name='delete order'),
    path('deleteallorders/<int:pk>', delete_all_orders, name='delete all orders'),
]