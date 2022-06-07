# Подключаем компонент для работы с формой
from django import forms
# Подключаем компонент UserCreationForm
from django.contrib.auth.forms import UserCreationForm
# Подключаем модель User
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# Создаём класс формы
class RegistrFormStudent(UserCreationForm):
  # Добавляем новое поле Email
  name = forms.CharField(max_length=200)
  surname = forms.CharField(max_length=200)
  email = forms.EmailField(max_length=254, help_text='This field is required')
  CHOICES=[
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
    ('11', '11'),
  ]
  clas = forms.ChoiceField(choices=CHOICES)
  # Создаём класс Meta
  class Meta:
    # Свойство модели User
    model = User
    # Свойство назначения полей
    fields = ('username', 'name', 'surname', 'clas', 'email', 'password1', 'password2', )


class RegistrFormTeacher(UserCreationForm):
  # Добавляем новое поле Email
  name = forms.CharField(max_length=200)
  surname = forms.CharField(max_length=200)
  email = forms.EmailField(max_length=254, help_text='This field is required')
 # Создаём класс Meta
  class Meta:
    # Свойство модели User
    model = User
    # Свойство назначения полей
    fields = ('username', 'name', 'surname', 'email', 'password1', 'password2', )