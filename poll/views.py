from django.shortcuts import render, reverse
from django.http import HttpResponse
# Create your views here


def home(request):
    return render(request, "home.html", {})
# def register(request):
#     return HttpResponse("asdfasdf", status=200)
# Подключение для рендера
from django.shortcuts import render
# Подключение стандартной формы для регистрации
from django.contrib.auth.forms import UserCreationForm
# Подключение новой формы для регистрации
from .forms import RegistrFormStudent, RegistrFormTeacher
from django.shortcuts import redirect

def regist(request):
    data = {}
    form = ''
    if request.method == "GET":
        role = ""
        if request.GET.get("role", "") == "student":
            role = "student"
            form = RegistrFormStudent()
        elif request.GET.get("role", "") == "teacher":
            role = "teacher"
            form = RegistrFormTeacher()
        data["form"] = form
        response = render(request, 'registr.html', data)
        response.set_cookie('role', role)
        return response

    if request.COOKIES.get('role') == 'student':
        form = RegistrFormStudent(request.POST) # для ученика
    elif request.COOKIES.get('role') == "teacher":
        form = RegistrFormTeacher(request.POST) # для учителя
    # Валидация данных из формы
    if form.is_valid():
        # Сохраняем пользователя
        form.save()
        # Передача формы к рендару
        data['form'] = form
        # Передача надписи, если прошло всё успешно
        data['res'] = "Всё прошло успешно"
        # Рендаринг страницы    
        return redirect('/')
    else:
        print("Форма не валидна")
        if request.COOKIES.get('role') == 'student':
            form = RegistrFormStudent() # для ученика
        elif request.COOKIES.get('role') == "teacher":
            form = RegistrFormTeacher() # для учителя
        return render(request, 'registr.html', {"form":form, "res":"Все фигня, переделывай"})
    return render(request, 'registr.html', data)