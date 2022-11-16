from django.http import HttpResponse
from django.shortcuts import render

menu = [{'title': "Animals", 'url_name': 'animals'}]


def index(request):
    context = {
        'menu': menu,
        'title': 'Animal Shelter'
    }
    return render(request, 'shelter/index.html', context=context)


def animals(request):
    context = {
        'menu': menu,
        'title': 'Animals'
    }
    return render(request, 'shelter/index.html', context=context)


def register(request):
    context = {
        'menu': menu,
        'title': 'Register'
    }
    return render(request, 'shelter/index.html', context=context)


def login(request):
    context = {
        'menu': menu,
        'title': 'Log in'
    }
    return render(request, 'shelter/index.html', context=context)


def userpage(request):
    context = {
        'menu': menu,
        'title': 'User page'
    }
    return render(request, 'shelter/index.html', context=context)
