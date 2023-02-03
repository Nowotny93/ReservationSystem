from django.urls import path

from reservation_system.common.views import landing_page

urlpatterns = [
    path('', landing_page, name='index'),
]