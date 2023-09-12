#для хранения приложения текущего представления
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Страница приложения women")

def categories(request):
    return HttpResponse("<h1> статьи по категориям </h1>")

def categories1(request):
    return HttpResponse("<h1> Категории запросов пользователя </h1>")