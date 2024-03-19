from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from main.models import todo, Profile


class TodoAddPageForm(forms.ModelForm):

    class Meta:
        model = todo
        fields = ('title','content', 'photo')
class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин',widget=forms.TextInput())
    password = forms.CharField(label="Пароль",widget=forms.PasswordInput())

class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Логин',widget=forms.TextInput())
    email = forms.EmailField(label='Почта',widget=forms.EmailInput(attrs={}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Повтор Пароля", widget=forms.PasswordInput())

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar','bio')
        widgets = {'user': forms.HiddenInput()}