from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class LoginForm(forms.Form):
    email = forms.CharField(required=True, label='Email')
    password = forms.CharField(required=True, label='Пароль', widget=forms.PasswordInput)


class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', strip=False, required=True, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Подтвердите пароль', strip=False, required=True,
                                       widget=forms.PasswordInput)
#
#     class Meta:
#         model = get_user_model()
#         fields = ('username', 'password', 'password_confirm', 'first_name', 'last_name', 'email', "phone")
#
#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get('password')
#         password_confirm = cleaned_data.get('password_confirm')
#         if password and password_confirm and password != password_confirm:
#             raise forms.ValidationError('Пароли не совпадают!')
#
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data.get('password'))
#         if commit:
#             user.save()
#         return user
#
#
# class UserChangeForm(forms.ModelForm):
#     class Meta:
#         model = get_user_model()
#         fields = ('first_name', 'last_name', 'email', 'phone')
#         labels = {'first_name': 'Имя', 'last_name': 'Фамилия', 'email': 'Email', 'phone': 'телефон'}
#
#
#
