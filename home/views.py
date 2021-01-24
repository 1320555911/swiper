# -*- coding: utf-8 -*-
# @File    : api.py
# @Theme   ：
# @Time    : 2021/1/24 21:24
# @Author  :xiaowu
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')