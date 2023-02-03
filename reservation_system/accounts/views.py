from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, FormView

from reservation_system.accounts.forms import LoginForm, RegisterForm, ProfileForm
from reservation_system.accounts.models import Profile
from reservation_system.inventory.models import Table
from reservation_system.menu.models import Menu


class LoginUserView(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = LoginForm

    def get_success_url(self):
        return reverse('list tables')


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)

        return result


def logout_user(request):
    logout(request)
    return redirect('index')


class ProfileDetailsView(LoginRequiredMixin, FormView):
    template_name = 'accounts/user_profile.html'
    form_class = ProfileForm
    success_url = reverse_lazy('profile details')
    object = None

    def get(self, request, *args, **kwargs):
        self.object = Profile.objects.get(pk=request.user.id)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = Profile.objects.get(pk=request.user.id)
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        self.object.profile_image = form.cleaned_data['profile_image']
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['tables'] = Table.objects.filter(user_id=self.request.user.id)
        context['products'] = Menu.objects.filter(user_id=self.request.user.id)
        context['profile'] = self.object

        return context
