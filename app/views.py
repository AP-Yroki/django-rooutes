from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, \
    HttpResponsePermanentRedirect, HttpResponseBadRequest, \
    HttpResponseForbidden, JsonResponse, HttpResponseNotFound

from django.core.serializers.json import DjangoJSONEncoder


def index(request):
    username = request.GET['username']
    password = request.GET['password']
    return HttpResponse(f'Логин: {username}, <br> Пароль: {password}')
def posts(request):
    return HttpResponse(f'Весь набор постов')

def new(request):
    return HttpResponse('Последние опубликованные посты')

def top(request):
    return HttpResponse('Наиболее популяные посты')

def comments(request, id):
    return HttpResponse(f'Коментарии поста {id}')

def likes(request, id):
    return HttpResponse(f'Лайки поста {id}')

def user(request):
    age = request.GET.get('age', 0)
    name = request.GET.get('name', "Unvelivable")
    return HttpResponse(f'<h2>Имя: {name} Возраст: {age}</h2>')

def about(request):
    return HttpResponse('About')

def contacts(request):
    return HttpResponse('About')

def redirect_about(request):
    return HttpResponseRedirect('/about')

def pernament_redirect_about(request):
    return HttpResponsePermanentRedirect('/about')

def redirect_contacts(request):
    return HttpResponseRedirect('/contacts')

def pernament_redirect_contacts(request):
    return HttpResponsePermanentRedirect('/contacts')

def details(request):
    return HttpResponsePermanentRedirect('/')

def page_not_found(request, status_code):
    return HttpResponseNotFound('Загрузка страницы была завершена ошибкой')


def page_not_found(request):
    status_code = request.GET.get('status_code')
    if status_code == '404':
        return HttpResponseNotFound('Загрузка страницы была завершена ошибкой')
    else:
        return HttpResponseForbidden('Загрузка страницы прошла без ошибок')


def access(request):
    username = request.GET.get('username', 'Unverified')
    password = request.GET.get('password', 'Unverified')

    if username == 'admin' and password == 'admin':
        return HttpResponse('Всё норм')
    else:
        return HttpResponseForbidden(
            'Отсутствует доступ, повторите попытку.')

def set(request):
    username = request.GET.get('username', "unvelivable")
    response = HttpResponse(f'Hello {username}!')
    response.set_cookie('username', username)
    return response

def get(request):
    username = request.COOKIES['username']
    return HttpResponse(f'Hello {username}')


def json(request):
    return JsonResponse({'name': 'Tom', 'age': 38})