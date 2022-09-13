from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                          'placeholder': 'Введите почту'}))

    username = forms.CharField(required=True, label='Введите логин', help_text='Нельзя вводить символы @, /, _.',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите логин'}))

    password1 = forms.CharField(required=True, label='Введтие пароль', help_text='Пароль должен быть длинным',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    password2 = forms.CharField(required=True, label='Введтие пароль', help_text='Подтвердите пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password1']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                          'placeholder': 'Введите почту'}))

    username = forms.CharField(required=True, label='Введите логин', help_text='Нельзя вводить символы @, /, _.',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите логин'}))

    class Meta:
        model = User
        fields = ['email', 'username']
class ProfileImageForm(forms.ModelForm):
    img=forms.ImageField(
        label="Загрузить фото",
        required=True

    )
    class Meta:
        model=Profile
        fields=['img']