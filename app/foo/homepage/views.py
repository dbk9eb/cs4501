# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hello, World!</h1>")
    #context = {'message': 'Hello, World!'}
    #return render(request, 'homepage/index.html', context)
