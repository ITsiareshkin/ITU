from django.http import HttpResponse
from django.shortcuts import render

menu = [{'title': "Animals", 'url_name': 'animals'},
        {'title': "About Us", 'url_name': 'about_us'},
        {'title': "Donate", 'url_name': 'donate'},
        {'title': "Sign In", 'url_name': 'sign_in'}
]

def index(request):
    context = {
        'menu': menu,
        'title': 'Animal Shelter'
    }
    return render(request, 'shelter/index.html', context=context)

def userpage(request):
    return render(request, 'shelter/index.html')

def about_us(request):
    return render(request, 'shelter/index.html')

def animals(request):
    return render(request, 'shelter/index.html')

def donate(request):
    return render(request, 'shelter/index.html')