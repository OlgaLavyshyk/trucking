from django import forms
from django.core.exceptions import ValidationError
from .models import Request, Review
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AddRequest(forms.Form):
    name = forms.CharField(max_length=20)
    surname = forms.CharField(max_length=20)
    email = forms.EmailField()
    company = forms.CharField(max_length=30)
    message = forms.CharField(widget=forms.Textarea(), required=False)

    def clean_surname(self):
        name_data = self.cleaned_data['name']
        sur_data = self.cleaned_data['surname']

        if name_data == sur_data:
            raise ValidationError("Enter correct data")

        return sur_data


class AddRequestModelForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ("name", "surname", "email", "company", "message")


class AddUserForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("name", "message", "email")


# Создаём класс формы
class RegistrForm(UserCreationForm):
    # Добавляем новое поле Email
    email = forms.EmailField(max_length=254, help_text='This field is required')

    # Создаём класс Meta
    class Meta:
        # Свойство модели User
        model = User
        # Свойство назначения полей
        fields = ('username', 'email', 'password1', 'password2')


