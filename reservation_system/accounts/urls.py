from django.urls import path

from reservation_system.accounts.views import LoginUserView, RegisterView, logout_user, ProfileDetailsView

urlpatterns = (
    path('login/', LoginUserView.as_view(), name='log in user'),
    path('register/', RegisterView.as_view(), name='register user'),
    path('logout/', logout_user, name='log out user'),
    path('', ProfileDetailsView.as_view(), name='profile details'),
)