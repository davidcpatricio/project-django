from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'David Patrício'
    })


def about(request):
    return HttpResponse('ABOUT')


def contact(request):
    return render(request, 'recipes/contact.html')
