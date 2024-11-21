from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import *

# class AddSurgeonForm(forms.Form):
#     title = forms.CharField(max_length=255, label="Имя")
#     birdhday = forms.DateField(label="Дата рождения ГГГГ-ММ-ДД")
#     is_published = forms.BooleanField(label="Публикация", required=False, initial=True)

class AddSurgeonForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['birdhday'].empty_label = "ГГГГ-ММ-ДД"

    class Meta:
        model = Surgeon
        fields = ['title', 'birdhday', 'is_published']

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2= forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
       
class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

class AddOperationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['surg'].empty_label = "Хирург не выбран"

    class Meta:
        model = OpeartionSchedule
        # fields = ['operationdate', 'surg']
        # fields = ('operationdate', 'surg',)
        fields = '__all__'