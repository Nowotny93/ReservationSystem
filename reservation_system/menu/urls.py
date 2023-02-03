from django.urls import path

from reservation_system.menu.views import MenuView, AddProductView, DeleteProductView, edit_product

urlpatterns = [
    path('', MenuView.as_view(), name='list menu'),
    path('addproduct/', AddProductView.as_view(), name='add product'),
    path('editproduct/<int:pk>', edit_product, name='edit product'),
    path('deleteproduct/<int:pk>', DeleteProductView.as_view(), name='delete product'),
]
