from django import forms
from .models import Seller, Product
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class UpdateProfile(forms.ModelForm):
    age=forms.IntegerField()

    def clean_age(self):
        if self.cleaned_data['age']<18:
            raise ValidationError('Возвращайтесь когда вам исполнится 18 лет')
        return self.cleaned_data['age']

    class Meta:
        model = Seller
        fields = '__all__'


class UpdateGoods(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ["title", "slug"]

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')