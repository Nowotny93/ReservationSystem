from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from reservation_system.accounts.models import Profile
from reservation_system.core.forms import BootstrapFormMixin

UserModel = get_user_model()


class LoginForm(AuthenticationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'


class RegisterForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email', 'username', 'password1')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        del self.fields['password2']
        self.fields['password1'].help_text = None
        self.fields['username'].help_text = None

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'




class ProfileForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_image',)
