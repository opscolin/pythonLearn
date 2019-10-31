# -*- encoding: utf-8 -*-
"""
@File:      urls.py
@Time:      2019/10/31 下午10:55
@Author:    Colin
@Email:     bsply@126.com
@Software:  PyCharm
"""


from django.urls import path

from cookie.views import login, index, logout
urlpatterns = [
    path('login/', login, name='login'),
    path('', index, name='index'),
    path('logout', logout, name='logout'),
]
