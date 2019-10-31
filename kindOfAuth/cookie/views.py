from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

import datetime


# Create your views here.
def cookie_auth(func):
    """
    cookie 登录认证装饰器
    """

    def wrapper(request, *args, **kwargs):
        cookie = request.COOKIES.get('user')
        if cookie:
            res = func(request, *args, **kwargs)
            return res
        else:
            return JsonResponse({'msg': 'cookie auth failed'})

    return wrapper


def login(request):
    """
    登录设置Cookie
    """
    msg = ''
    if request.method == 'POST':
        username = request.POST.get("username", False)
        password = request.POST.get("password", False)
        if username == 'root' and password == 'root1203':
            print(username, password)
            res = redirect('index')
            # http_only
            # max_age
            # res.set_cookie("user", username, expires=datetime.timedelta(seconds=200), path='/cookie/', domain='127.0.0.1')
            res.set_cookie("user", username)
            # dict_values([('Content-Type', 'text/html; charset=utf-8'), ('Location', '/cookie/')])
            print(res.items())
            # b'Content-Type: text/html; charset=utf-8\r\nLocation: /cookie/'
            print(res.serialize_headers())
            # Cookies:  Set-Cookie: user=root; Path=/
            print('Cookies: ', res.cookies)
            # ''
            print(res.content)
            # 302
            print(res.status_code)
            # True
            print(res.has_header('Cookie'))
            return res
        else:
            msg = 'no such username or password is wrong!'
    return render(request, 'cookie/login.html', {'msg': msg})


@cookie_auth
def index(request):
    return JsonResponse({'msg': 'Hello Cookies Testing'})


def logout(request):
    """
    登出删除Cookies
    """
    res = redirect('index')
    res.delete_cookie('user')
    print('Cookie: ', res.cookies)
    return res
